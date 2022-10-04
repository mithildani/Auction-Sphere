import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from sqlite3 import Error
from datetime import datetime

app = Flask(__name__)
CORS(app)

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

@app.route("/bid/create", methods=["POST"])
def create_bid():
    # Get relevant data
    productId=request.get_json()['prodId']
    email=request.get_json()['email']
    amount=request.get_json()['bidAmount']

    # create db connection
    conn = create_connection(database)
    c = conn.cursor()

    # get initial price wanted by seller
    select_query="SELECT initial_price FROM product WHERE prod_id='" + str(productId) + "';"
    c.execute(select_query)
    result = list(c.fetchall())
    response = {}

    #  if bid amount is less than price by seller then don't save in db
    if (result[0][0]>(int)(amount)):
        response["message"]= "Amount less than initial price"
    else:
        currentTime= int(datetime.utcnow().timestamp())
        # print(currentTime)
        insert_query= "INSERT OR REPLACE INTO bids(prod_id,email,bid_amount,created_at) VALUES ('" + str(productId) + "','" + \
                      str(email) + "','" + str(amount) + "','" + str(currentTime) + "');"
        c.execute(insert_query)
        conn.commit()

        response["message"]="Saved Bid"
    return jsonify(response)

@app.route("/product/create", methods=["POST"])
def create_product():
    productName = request.get_json()['name']
    sellerEmail = request.get_json()['seller_email']
    initialPrice = request.get_json()['initial_price']
    increment = request.get_json()['increment']
    deadlineDate = request.get_json()['deadline_date']
    description = request.get_json()['description']
    
    conn = create_connection(database)
    c = conn.cursor()
    response = {}
    currentTime= int(datetime.utcnow().timestamp())
    print (os.getcwd()) 
    # os.path.expanduser('~')
    # # photo_loc = os.path.expanduser('~/Desktop/Sem 1/SE/project/Auction-Sphere/backend/photos/photo1.jpeg')
    photo_loc = 'photos/photo1.jpeg'
    empPhoto = convertToBinaryData(photo_loc)
    query = "INSERT INTO product(name, seller_email, photo, initial_price, date, increment, deadline_date, description) VALUES (?,?,?,?,?,?,?,?)"
    c.execute(query,('" + str(productName) + "','" + str(sellerEmail) + "',empPhoto," + str(initialPrice) + ",'" + str(currentTime) + "'," + str(increment) + ",'" + str(deadlineDate) + "','" + str(description) + "'))
    conn.commit()
    response["result"] = "Added product successfully"

    query = "SELECT * FROM product WHERE prod_id = 1"
    c.execute(query)



    return response

@app.route("/product/listAll", methods=["GET"])
def get_all_products(): 
    query = "SELECT * FROM product ORDER BY date DESC"
    conn = create_connection(database)
    c = conn.cursor()
    c.execute(query)
    result = list(c.fetchall())
    response = {"result": result}
    return(response)

@app.route("/product/getDetails", methods=["POST"])
def get_product_details():
    productID = request.get_json()['productID']
    
    conn = create_connection(database)
    c = conn.cursor()

    # gets product details
    query = "SELECT * FROM product WHERE prod_id=" + str(productID) + ";"
    c.execute(query)
    result = list(c.fetchall())

    # get highest 10 bids 
    query = "SELECT first_name, last_name, (SELECT bid_amount FROM bids WHERE prod_id=" + str(productID) + " AND bids.email = users.email ORDER BY bid_amount DESC LIMIT 10) bid_amount FROM users ORDER BY bid_amount DESC;"
    c.execute(query)
    topbids = list(c.fetchall())
    
    response = {"product": result, "bids": topbids}
    return response

@app.route("/product/update", methods=["POST"])
def update_product_details():
    productId = request.get_json()['productID']
    productName = request.get_json()['productName']
    initialPrice = request.get_json()['initialPrice']
    deadlineDate = request.get_json()['deadlineDate']
    description = request.get_json()['description']
    increment = request.get_json()['increment']

    query = "UPDATE product SET name='" + str(productName) + "',initial_price='" + str(initialPrice) + "',deadline_date='" + str(deadlineDate) + "',increment='" + str(increment) + "',description='" + str(description) + "' WHERE prod_id=" + str(productId) + ";"
    print(query)
    conn = create_connection(database)
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    response = {"result": "Updated product successfully"}
    return response

database = r"auction.db"
# write queries for creating database here:
create_users_table = """CREATE TABLE IF NOT EXISTS users( first_name TEXT NOT NULL, last_name TEXT NOT NULL, contact_number TEXT NOT NULL UNIQUE, email TEXT UNIQUE PRIMARY KEY, password TEXT NOT NULL);"""

create_product_table = """CREATE TABLE IF NOT EXISTS product(prod_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, photo BLOB, seller_email TEXT NOT NULL, initial_price REAL NOT NULL, date INTEGER NOT NULL, increment REAL, deadline_date INTEGER NOT NULL, description TEXT,  FOREIGN KEY(seller_email) references users(email));"""

create_bids_table = """CREATE TABLE IF NOT EXISTS bids(prod_id INTEGER, email TEXT NOT NULL , bid_amount REAL NOT NULL, created_at TEXT NOT NULL, FOREIGN KEY(email) references users(email), FOREIGN KEY(prod_id) references product(prod_id), PRIMARY KEY(prod_id, email));"""

create_table_claims = """CREATE TABLE IF NOT EXISTS claims(prod_id INTEGER, email TEXT NOT NULL, expiry_date TEXT NOT NULL, claim_status INTEGER, FOREIGN KEY(email) references users(email), FOREIGN KEY(prod_id) references product(prod_id));"""

conn = create_connection(database)
if conn is not None:
    create_table(conn, create_users_table)
    create_table(conn, create_product_table)
    create_table(conn, create_bids_table)
    create_table(conn, create_table_claims)
else:
    print("Error! Cannot create the database connection")



if __name__ == "__main__":
  app.debug = True
  app.run()
