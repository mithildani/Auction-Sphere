import os
from models import Product, Bids, db
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from flask_caching import Cache
from cacheHandler.productcache import ProductCache
from sqlalchemy import func
from flask_cors import CORS
from config import settings
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from flask_mail import Mail, Message as MailMessage
from flask_migrate import Migrate

import sys
sys.path.append("..")
from userms.models import Users


app = Flask(__name__)
CORS(app, support_credentials=True)
app.config.from_object(settings[os.environ.get('APPLICATION_ENV', 'default')])

mail = Mail(app)
cache = Cache(app)

db.init_app(app)
migrate = Migrate(app, db)


def convertToBinaryData(filename):
    # Convert digital data to binary format

    print(filename)
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


@app.route("/bid/create", methods=["POST"])
def create_bid():
    """ 
    API end point to create a new bid.
    This API allows users to bid on a product which is open for auctioning.
    Details like productId, user_id, and new bid amount are extracted from the json.
    Then on the basis of productId, initial price of the product is checked to validate if the new bid amount is greater than the initial amount.
    If the bid amount is lesser than the value extracted in the previous row, then the bid isn't created/updated. 
    Otherwise it is created/updated.
    """
    # Get relevant data
    productId = request.get_json()['prodId']
    user_id = request.get_json()['user_id']
    amount = request.get_json()['bidAmount']

    price_cache = ProductCache(prodId = productId)
    price_cache.get_configuration()

    price = price_cache.initial_price
    response = {}

    #  if bid amount is less than price by seller then don't save in db
    if (price > (float)(amount)):
        response["message"] = "Amount less than initial price"
    else:
        currentTime = int(datetime.utcnow().timestamp())
        bid = Bids()
        bid.prod_id = productId
        bid.user_id = user_id
        bid.bid_amount = amount
        bid.created_at = currentTime
        db.session.add(bid)
        db.session.commit()
        db.session.refresh(bid)
        response["message"] = "Saved Bid"
    return jsonify(response)


@app.route("/product/create", methods=["POST"])
def create_product():
    """ 
    API end point for new product creation.
    This API is used to create new entries for the products open for auctioning.
    Here, productName, sellerEmail, initialPrice, increment, photo(byte 64 encoded) and product description are extracted from the json.
    These values are entered into the product table.
    """
    productName = request.get_json()['productName']
    seller_id = request.get_json()['seller_id']
    initialPrice = request.get_json()['initialPrice']
    increment = request.get_json()['increment']
    photo = request.get_json()['photo']
    description = request.get_json()['description']

    response = {}
    currentTime = int(datetime.utcnow().timestamp())
    currentTime = datetime.fromtimestamp(currentTime)
    deadlineDate = currentTime + timedelta(days=7)
    print(deadlineDate)

    product = Product()
    product.name = productName
    product.seller_id = seller_id
    product.initial_price = initialPrice
    product.increment = increment
    product.photo = photo
    product.description = description
    product.date = currentTime
    product.deadline_date = deadlineDate
    db.session.add(product)
    db.session.commit()
    db.session.refresh(product)
    response["result"] = "Added product successfully"

    return response


@app.route("/product/listAll", methods=["GET"])
def get_all_products():
    """ 
    API end point to list all the products.
    This API lists down all the product details present in product table sorted in the descending order of date created.
    """
    instance = Product.query.order_by(Product.date.desc()).all()
    result = list(instance)
    response = {"result": result}
    return(response)


@app.route("/product/getImage", methods=["POST"])
def get_product_image():
    """ 
    API end point to get image from product ID.
    This API is used to get image of the product on the basis of productId extracted from the json.
    This returns photo from the product table.
    """
    productId = request.get_json()['productID']

    photo_cache = ProductCache(prodId = productId)
    photo_cache.get_configuration()
    picture = photo_cache.photo

    result = list(picture)
    response = {"result": result}
    return response


@app.route("/product/getDetails", methods=["POST"])
def get_product_details():
    """ 
    API end point to details of a product from product ID.
    This API is used to get details of the product on the basis of productId extracted from json.
    This returns all the details from from the product table.
    It also lists down top ten bids of a particular product.
    """
    productID = request.get_json()['productID']
    instance = Product.query.filter_by(prod_id=productID).all()
    result = list(instance)

    instance = Users.query.join(Bids). \
        with_entities(Users.first_name, Users.last_name, Bids.bid_amount). \
        filter(Bids.prod_id == productID). \
        order_by(Bids.bid_amount.desc())[:10]
    topbids = list(instance)

    response = {"product": result, "bids": topbids}
    return response


@app.route("/product/update", methods=["PUT"])
def update_product_details():
    """ 
    API end point to update a product.
    This API is used while updating the details of a product.
    User provides productId, productName, initialPrice, deadlineDate, description and increment value which is extracted from the json.
    These new values are updated in the product table on the basis of productId.
    """

    productId = request.get_json().get('productID')
    productName = request.get_json().get('productName')
    initialPrice = request.get_json().get('initialPrice')
    deadlineDate = request.get_json().get('deadlineDate')
    description = request.get_json().get('description')
    increment = request.get_json().get('increment')

    instance = Product.query.filter_by(prod_id=productId).first()
    instance.update(dict(name=productName, initial_price=initialPrice,
                         deadline_date=deadlineDate, increment=increment, description=description))

    productcache = ProductCache(prodId = productId)
    productcache.initial_price = initialPrice
    productcache.name = productName
    productcache.deadline_date = deadlineDate
    productcache.increment = increment
    productcache.description = description
    productcache._save_config_to_cache()

    response = {"message": "Updated product successfully"}
    return response



# if pageSize> num of rows then error
@app.route("/getLatestProducts", methods=["GET"])
def get_landing_page():
    """ 
    API end point to get top ten latest products.
    This API extracts details of the top products sorted by descending order of date created.
    It also fetches the highest bids on the those products from the bids table and the user details from the user table.
    If there is no such bid on the product, -1 is appended to the list.
    """

    pageNum = int(request.args.get('pageNum'))
    pageSize = int(request.args.get('pageSize'))
    offset = ((pageNum-1)*pageSize)
    response = {}

    instance = Product.query \
        .with_entities(Product.prod_id, Product.name, 
                        Product.seller.email, Product.initial_price, 
                        Product.date, Product.increment, 
                        Product.deadline_date, Product.description
                        ) \
        .order_by(Product.date.desc()) \
        .limit(pageSize) \
        .offset(offset)
    products = list(instance)
    num=Product.query.count()
    totalProducts = num

    # other details of products
    highestBids = []
    names = []
    for product in products:
        instance=Bids.query().with_entities(Bids.email, func.max(Bids.bid_amount)).filter_by(prod_id=product[0]).scalar()
        result = list(instance)
        if(result[0][0] != None):
            result = result[0]
            highestBids.append(result[1])
            ins=Users.query.with_entities(Users.first_name, Users.last_name).filter_by(email=result[0])
            names.append(list(ins[0]))
        else:
            highestBids.append(-1)
            names.append("N/A")
    response = {
        "products": products, 
        "maximumBids": highestBids,
        "names": names, 
        "total": totalProducts
    }
    print(response)
    return jsonify(response)


def mail_job():
    with app.app_context():
        # fetch products with expired deadline, email not yet sent
        instance = Product.query \
            .with_entities(Product.prod_id, Product.name, Product.seller_email, Product.deadline_date, Product.email_sent) \
            .filter(Product.email_sent==0, Product.deadline_date <= datetime.now().date()) \
            .order_by(Product.date.desc())
        products = list(instance)

        print("Products with expired deadline")
        print(products)

        for product in products:
            print("----- Product with expired deadline -----")
            print(product)
            # send email to highest bidder and product owner
            instance=Bids.query.with_entities(Bids.user.email, func.max(Bids.bid_amount)).filter_by(prod_id=product[0]).scalar()
            result = list(instance)

            print("Check highest bidder")
            print(result)

            if(result[0][0] != None):
                print("Highest bidder found")
                result = result[0]
                send_email(
                    str(result[0]), 
                    f"Congratulations, the product {str(product[1])} has been successfully claimed by you!"
                )
                send_email(
                    str(product[2]), 
                    f"Congratulations, the product {str(product[1])} has been successfully claimed!"
                )
            else:
                print("No bidder found")
                # if not claimed, send email to product owner
                send_email(str(product[2]), "Sorry, your product was not claimed by anyone.")
            
            print("Update email sent")
            instance = Product.query.filter_by(prod_id=product[0]).first()
            instance.update(dict(email_sent=1))

            
def send_email(recipient, message):
    print("Email job started")
    print(recipient)
    print(message)
    try:
        with app.app_context():
            msg = MailMessage(
                'Knock knock, its Auction Sphere! We have a notification for you.', 
                sender =  'slackpoint.developers@gmail.com', 
                recipients = [recipient]
            )
            msg.body = message
            mail.send(msg)
            print("Email sent!")
    except Exception as e:
        print(e)

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(mail_job, 'interval', minutes=1)
scheduler.start()

if __name__ == "__main__":
    app.debug = True
    app.run()

atexit.register(lambda: scheduler.shutdown())