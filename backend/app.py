from models import *
from datetime import datetime, timedelta
import os
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from flask_caching import Cache
from cacheHandler.basecache import BaseCacheHandler
from cacheHandler.product_cache import Product_Cache
import json
from sqlalchemy import func
# from flask_cors import CORS
from models import db
from env_config import Config
import sqlite3
import sys
sys.path.append("..")

cache_config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "RedisCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_REDIS_HOST": 'localhost',
    "CACHE_REDIS_PORT":'6379',
    "CACHE_REDIS_URL": 'redis://localhost:6379/0'
}

import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from flask_mail import Mail, Message as MailMessage
from env_config import Config



app = Flask(__name__)

app.config['MAIL_SERVER']=Config.MAIL_SERVER
app.config['MAIL_PORT'] = Config.MAIL_PORT
app.config['MAIL_USERNAME'] = Config.MAIL_EMAIL_ADDRESS
app.config['MAIL_PASSWORD'] = Config.MAIL_APP_PASSWORD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['TESTING'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ECHO'] = Config.SQLALCHEMY_ECHO
# app.config['SQLALCHEMY_BINDS'] = Config.SQLALCHEMY_BINDS
mail = Mail(app)

# CORS(app)
app.config.from_mapping(cache_config)
db.init_app(app)
cache = Cache(app)

def create_connection(db_file):
  conn = None
  conn = sqlite3.connect(db_file)
  return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

def convertToBinaryData(filename):
    # Convert digital data to binary format

    print(filename)
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

database = r"auction.db"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

""" 
API end point for user creation.
It extracts firstName, lastName, email, contact number and password from the json.
This further checks if the email provided is already there in the database or not.
If the account is already created, the API returns (An account with this contact already exists) 
otherwise, a new user is created in the users table with all the details extracted from json. 
"""
@app.route("/signup", methods=["POST"])
def signup(): 
    firstName = request.get_json()['firstName']
    lastName = request.get_json()['lastName']
    email = request.get_json()['email']
    contact = request.get_json()['contact']
    password = request.get_json()['password']

    conn = create_connection(database)
    c = conn.cursor()
    
    #check if email already exists 
    query = "SELECT COUNT(*) FROM users WHERE email='" + str(email) + "';"
    c.execute(query)

    result = list(c.fetchall())
    response = {}
    if(result[0][0] == 0): 
        query = "SELECT COUNT(*) FROM users WHERE contact_number='" + str(contact) + "';"
        c.execute(query)
        result = list(c.fetchall())

        if(result[0][0] != 0): 
            response["message"] = "An account with this contact already exists"
        else:
            query = "INSERT INTO users(first_name, last_name, email, contact_number, password) VALUES('" + str(firstName) + "','" + str(lastName) + "','" + str(email) + "','" + str(contact) + "','" + str(password) +"');"
            c.execute(query)
            conn.commit()
            response["message"] = "Added successfully"
    else: 
        response["message"] = "An account with this email already exists"
    return response

""" 
API end point for user login.
User email and password are extracted from the json.
These are validated from the data already available in users table.
If the email and password are correct, login is successful else user is asked to create an account.
"""
@app.route("/login", methods=["POST"])
def login(): 
    email = request.get_json()['email']
    password = request.get_json()['password']
    
    conn = create_connection(database)
    c = conn.cursor()
    
    # check if email and password pair exists
    query = "SELECT * FROM users WHERE email='" + str(email) + "' AND password='" + str(password) + "';"
    c.execute(query)
    result = list(c.fetchall())
    response = {}

    if(len(result) == 1): 
        response["message"] = "Logged in successfully"
    else: 
        # check if email exists, but password is incorrect
        query = "SELECT COUNT(*) FROM users WHERE email='" + str(email) + "';"
        c.execute(query)
        result = list(c.fetchall())
        if(result[0][0] == 1): 
            response["message"] = "Invalid credentials!"
        else: 
            response["message"] = "Please create an account!"
    return jsonify(response)

""" 
API end point to create a new bid.
This API allows users to bid ona product which is open for auctioning.
Details like productId, email, and new bid amount are extracted from the json.
Then on the basis of productId, initial price of the product is checked to validate if the new bid amount is greater than the initial amount.
If the bid amount is lesser than the value extracted in the previous row, then the bid isn't created/updated. 
Otherwise it is created/updated.
"""


@app.route("/bid/create", methods=["POST"])
def create_bid():
    # Get relevant data
    productId = request.get_json()['prodId']
    email = request.get_json()['email']
    amount = request.get_json()['bidAmount']

    # create db connection
    # conn = create_connection(database)
    # c = conn.cursor()

    # bid_cache = Create_Bid(cache, prodId = productId)
    # bid_cache.get_configuration()
    

    # get initial price wanted by seller
    # select_query = "SELECT initial_price FROM product WHERE prod_id='" + \
    #     str(productId) + "';"
    # # c.execute(select_query)
    # result = list(c.fetchall())

    price_cache = Product_Cache(prodId = productId)
    price_cache.get_configuration()

    price = price_cache.initial_price
    response = {}

    #  if bid amount is less than price by seller then don't save in db
    if (price > (float)(amount)):
        response["message"] = "Amount less than initial price"
    else:
        currentTime = int(datetime.utcnow().timestamp())
        # print(currentTime)
        # insert_query = "INSERT OR REPLACE INTO bids(prod_id,email,bid_amount,created_at) VALUES ('" + str(productId) + "','" + \
        #     str(email) + "','" + str(amount) + \
        #     "','" + str(currentTime) + "');"
        # c.execute(insert_query)
        bid = Bids()
        bid.prod_id = productId
        bid.email = email
        bid.bid_amount = amount
        bid.created_at = currentTime
        db.session.add(bid)
        db.session.commit()
        db.session.refresh(bid)
        response["message"] = "Saved Bid"
    return jsonify(response)


""" 
API end point for new product creation.
This API is used to create new entries for the products open for auctioning.
Here, productName, sellerEmail, initialPrice, increment, photo(byte 64 encoded) and product description are extracted from the json.
These values are entered into the product table.
"""


@app.route("/product/create", methods=["POST"])
def create_product():
    productName = request.get_json()['productName']
    sellerEmail = request.get_json()['sellerEmail']
    initialPrice = request.get_json()['initialPrice']
    increment = request.get_json()['increment']
    photo = request.get_json()['photo']
    description = request.get_json()['description']

    response = {}
    currentTime = int(datetime.utcnow().timestamp())
    currentTime = datetime.fromtimestamp(currentTime)
    deadlineDate = currentTime + timedelta(days=7)
    print(deadlineDate)

    # query = "INSERT INTO product(name, seller_email, photo, initial_price, date, increment, deadline_date, description) VALUES (?,?,?,?,?,?,?,?)"
    # c.execute(query, (str(productName), str(sellerEmail), str(
    #     photo), initialPrice, currentTime, increment, deadlineDate, str(description)))
    # conn.commit()

    product = Product()
    product.name = productName
    product.seller_email = sellerEmail
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


""" 
API end point to list all the products.
This API lists down all the product details present in product table sorted in the descending order of date created.
"""


@app.route("/product/listAll", methods=["GET"])
def get_all_products():
    # query = "SELECT prod_id, name, seller_email, initial_price, date, increment, deadline_date, description FROM product ORDER BY date DESC"
    # conn = create_connection(database)
    # c = conn.cursor()
    # c.execute(query)

    # product = []
    # for product in Product.query.all():
    #     product_cache = Get_Product(prodId = prod_id)
    #     product_cache.get_configuration()

    #     product.append({
    #         "prod_id":prod_id,
    #         "name":name,
    #         "seller_email":seller_email,
    #         "initial_price":initial_price,
    #         "date":date,
    #         "increment":increment,
    #         "deadline_date":deadline_date,
    #         "description":description
    #     })

    instance = Product.query.order_by(Product.date.desc()).all()
    result = list(instance)
    response = {"result": result}
    return(response)


""" 
API end point to get image from product ID.
This API is used to get image of the product on the basis of productId extracted from the json.
This returns photo from the product table.

"""


@app.route("/product/getImage", methods=["POST"])
def get_product_image():
    productId = request.get_json()['productID']
    # query = "SELECT photo FROM product WHERE prod_id=" + str(productId) + ";"
    # conn = create_connection(database)
    # c = conn.cursor()
    # c.execute(query)

    photo_cache = Product_Cache(prodId = productId)
    photo_cache.get_configuration()

    picture = photo_cache.photo

    # instance = Product.query.select(
    #     Product.photo).filter_by(prod_id=productId).first()
    result = list(picture)
    response = {"result": result}
    return response


""" 
API end point to details of a product from product ID.
This API is used to get details of the product on the basis of productId extracted from json.
This returns all the details from from the product table.
It also lists down top ten bids of a particular product.
"""


@app.route("/product/getDetails", methods=["POST"])
def get_product_details():
    productID = request.get_json()['productID']

    # conn = create_connection(database)
    # c = conn.cursor()

    # gets product details
    # query = "SELECT * FROM product WHERE prod_id=" + str(productID) + ";"
    # c.execute(query)
    # result = list(c.fetchall())

    instance = Product.query.filter_by(prod_id=productID).all()
    result = list(instance)

    # get highest 10 bids
    # query = "SELECT users.first_name, users.last_name, bids.bid_amount FROM users INNER JOIN bids ON bids.email = users.email WHERE bids.prod_id=" + \
    #     str(productID) + " ORDER BY bid_amount DESC LIMIT 10;"
    # c.execute(query)
    instance = Users.query.join(Bids). \
        with_entities(Users.first_name, Users.last_name, Bids.bid_amount). \
        filter(Bids.prod_id == productID). \
        order_by(Bids.bid_amount.desc())[:10]
    topbids = list(instance)

    response = {"product": result, "bids": topbids}
    return response


""" 
API end point to update a product.
This API is used while updating the details of a product.
User provides productId, productName, initialPrice, deadlineDate, description and increment value which is extracted from the json.
These new values are updated in the product table on the basis of productId.
"""

# changed post method to put method


@app.route("/product/update", methods=["PUT"])
def update_product_details():
    productId = request.get_json()['productID']
    productName = request.get_json()['productName']
    initialPrice = request.get_json()['initialPrice']
    deadlineDate = request.get_json()['deadlineDate']
    description = request.get_json()['description']
    increment = request.get_json()['increment']

    # query = "UPDATE product SET name='" + str(productName) + "',initial_price='" + str(initialPrice) + "',deadline_date='" + str(
    #     deadlineDate) + "',increment='" + str(increment) + "',description='" + str(description) + "' WHERE prod_id=" + str(productId) + ";"
    # print(query)
    # conn = create_connection(database)
    # c = conn.cursor()
    # c.execute(query)
    # conn.commit()

    instance = Product.query.filter_by(prod_id=productId).first()
    instance.update(dict(name=productName, initial_price=initialPrice,
                         deadline_date=deadlineDate, increment=increment, description=description))

    productcache = Product_Cache(prodId = productId)
    productcache.initialPrice = initialPrice
    productcache.name = name
    productcache.deadline_date = deadline_date
    productcache.increment = increment
    productcache.description = description
    productcache._save_config_to_cache

    response = {"message": "Updated product successfully"}
    return response


""" 
API end point to get top ten latest products.
This API extracts details of the top products sorted by descending order of date created.
It also fetches the highest bids on the those products from the bids table and the user details from the user table.
If there is no such bid on the product, -1 is appended to the list.
"""


@app.route("/getLatestProducts", methods=["GET"])
def get_landing_page():
    pageNum = request.args.get('pageNum')
    pageNum = int(pageNum)
    pageSize = request.args.get('pageSize')
    pageSize = int(pageSize)
    offset = ((pageNum-1)*pageSize)
    response = {}

    # fetch all products - paginated
    # query = "SELECT prod_id, name, seller_email, initial_price, date, increment, deadline_date, description FROM product ORDER BY date DESC LIMIT {limit} OFFSET {offset}"
    # query = query.format(limit=pageSize, offset=offset)
    # conn = create_connection(database)
    # c = conn.cursor()
    # c.execute(query)
    instance = Product.query.select(Product.prod_id, Product.name, Product.seller_email, Product.initial_price, Product.date,
                                    Product.increment, Product.deadline_date, Product.description).order_by(Product.date.desc()).limit(pageSize).offset(offset)

    products = list(instance)

    # fetch total count - for pagination component
    # query = "SELECT count(*) FROM product"
    # c.execute(query)
    num=Product.query.count()
    totalProducts = num

    # other details of products
    highestBids = []
    names = []
    for product in products:
        # query = "SELECT email, MAX(bid_amount) FROM bids WHERE prod_id=" + \
        #     str(product[0]) + ";"
        # c.execute(query)
        instance=Bids.query(func.max(Bids.bid_amount)).filter_by(prod_id=product[0]).scalar()
        result = list(instance)
        if(result[0][0] != None):
            result = result[0]
            highestBids.append(result[1])
            # query = "SELECT first_name, last_name FROM users WHERE email='" + \
            #     str(result[0]) + "';"
            # c.execute(query)
            ins=Users.query.select(Users.first_name, Users.last_name).filter_by(email=result[0])
            names.append(list(ins[0]))
        else:
            highestBids.append(-1)
            names.append("N/A")
    response = {"products": products, "maximumBids": highestBids,
                "names": names, "total": totalProducts}
    print(response)
    return jsonify(response)

database = r"auction.db"
drop_users_table = """DROP TABLE IF EXISTS users"""
create_users_table = """CREATE TABLE IF NOT EXISTS users( first_name TEXT NOT NULL, last_name TEXT NOT NULL, contact_number TEXT NOT NULL UNIQUE, email TEXT UNIQUE PRIMARY KEY, password TEXT NOT NULL);"""

drop_product_table = """DROP TABLE IF EXISTS product"""
create_product_table = """CREATE TABLE IF NOT EXISTS product(prod_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, photo TEXT, seller_email TEXT NOT NULL, initial_price REAL NOT NULL, date TIMESTAMP NOT NULL, increment REAL, deadline_date TIMESTAMP NOT NULL, description TEXT, email_sent INTEGER NOT NULL, FOREIGN KEY(seller_email) references users(email));"""

drop_bids_table = """DROP TABLE IF EXISTS bids"""
create_bids_table = """CREATE TABLE IF NOT EXISTS bids(prod_id INTEGER, email TEXT NOT NULL , bid_amount REAL NOT NULL, created_at TEXT NOT NULL, FOREIGN KEY(email) references users(email), FOREIGN KEY(prod_id) references product(prod_id), PRIMARY KEY(prod_id, email));"""

drop_claims_table = """DROP TABLE IF EXISTS claims"""
create_table_claims = """CREATE TABLE IF NOT EXISTS claims(prod_id INTEGER, email TEXT NOT NULL, expiry_date TEXT NOT NULL, claim_status INTEGER, FOREIGN KEY(email) references users(email), FOREIGN KEY(prod_id) references product(prod_id));"""

conn = create_connection(database)
if conn is not None:
    #create_table(conn, drop_users_table)
    create_table(conn, create_users_table)
    # create_table(conn, drop_product_table)
    create_table(conn, create_product_table)
    # create_table(conn, drop_bids_table)
    create_table(conn, create_bids_table)
    # create_table(conn, drop_claims_table)
    create_table(conn, create_table_claims)
else:
    print("Error! Cannot create the database connection")

def mail_job():
    # fetch products with expired deadline, email not yet sent
    query = "SELECT prod_id, name, seller_email, deadline_date, email_sent FROM product WHERE email_sent=0 AND deadline_date <= date('now')"
    conn = create_connection(database)
    c = conn.cursor()
    c.execute(query)
    products = list(c.fetchall())

    print("Products with expired deadline")
    print(products)

    for product in products:
        print("----- Product with expired deadline -----")
        print(product)
        # send email to highest bidder and product owner
        query = "SELECT email, MAX(bid_amount) FROM bids WHERE prod_id=" + str(product[0]) +";"
        c.execute(query)
        result = list(c.fetchall())

        print("Check highest bidder")
        print(result)

        if(result[0][0] != None):
            print("Highest bidder found")
            result = result[0]
            send_email(str(result[0]), "Congratulations, the product " + str(product[1]) + " has been successfully claimed by you!")
            send_email(str(product[2]), "Congratulations, the product " + str(product[1]) + " has been successfully claimed!")
        else:
            print("No bidder found")
            # if not claimed, send email to product owner
            send_email(str(product[2]), "Sorry, your product was not claimed by anyone.")
        
        print("Update email sent")
        query = "UPDATE product SET email_sent=1 WHERE prod_id=" + str(product[0]) +";"
        print(query)
        c.execute(query)
        conn.commit()
            
def send_email(recipient, message):
    print("Email job started")
    print(recipient)
    print(message)
    try:
        with app.app_context():
            msg = MailMessage('Knock knock, its Auction Sphere! We have a notification for you.', sender =  'slackpoint.developers@gmail.com', recipients = [recipient])
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