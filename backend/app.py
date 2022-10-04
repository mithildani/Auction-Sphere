from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from sqlite3 import Error

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
        query = "INSERT INTO users(first_name, last_name, email, contact_number, password) VALUES('" + str(firstName) + "','" + str(lastName) + "','" + str(email) + "','" + str(contact) + "','" + str(password) +"');"
        c.execute(query)
        conn.commit()
        response["result"] = "Added successfully"
    else: 
        response["result"] = "This email already exists"
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

@app.route("/create-bid", methods=["POST"])
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
        insert_query= "INSERT INTO bids(prod_id,email,bid_amount) VALUES ('" + str(productId) + "','" + str(email) + "','" + str(amount) +  "');"
        c.execute(insert_query)
        conn.commit()

        response["message"]="Saved Bid"
    return jsonify(response)

@app.route("/create-predict", methods=["POST"])
def create_product():
    #Get all the product details
    productId = request.get_json()['prod_id']
    productName = request.get_json()['name']
    sellerEmail = request.get_json()['seller_email']
    intialPrice = request.get_json()['initial_price']
    date = request.get_json()['date']
    increment = request.get_json()['increment']
    deadlineDate = request.get_json()['deadline_date']
    description = request.get_json()['description']
    
    conn = create_connection(database)
    c = conn.cursor()
    
    #check if product is already there
    query = "SELECT COUNT(*) FROM product WHERE productId ='" + str(productId) + "';"
    c.execute(query)
    
    result = list(c.fetchall())
    response = {}
    if(result[0][0] == 0): 
        query = "INSERT INTO product(prod_id, name, seller_email, initial_price, date, increment, deadline_date, description) VALUES('" + str(productId) + "','" + str(productName) + "','" + str(sellerEmail) + "','" + str(initialPrice) + "','" + str(date) + "','" + str(increment) + "','" + str(deadlineDate) + "','" + str(description) + "');"
        c.execute(query)
        conn.commit()
        response["result"] = "Added product successfully"
    else:
        response["result"] = "This product already exists"
    return response

database = r"auction.db"
#write queries for creating database here:
create_users_table = """CREATE TABLE users( first_name TEXT NOT NULL, last_name TEXT NOT NULL, contact_number TEXT NOT NULL UNIQUE, email TEXT UNIQUE PRIMARY KEY, password TEXT NOT NULL);"""

create_product_table = """CREATE TABLE product(prod_id INTEGER PRIMARY KEY, name TEXT NOT NULL, seller_email TEXT NOT NULL, initial_price REAL NOT NULL, date INTEGER NOT NULL, increment REAL, deadline_date INTEGER NOT NULL, description TEXT,  FOREIGN KEY(seller_email) references users(email));"""

create_bids_table = """CREATE TABLE bids(prod_id INTEGER, email TEXT NOT NULL , bid_amount REAL NOT NULL, FOREIGN KEY(email) references users(email), FOREIGN KEY(prod_id) references product(prod_id) PRIMARY KEY(prod_id, email);"""

create_table_claims = """CREATE TABLE claims(prod_id INTEGER, email TEXT NOT NULL, expiry_date TEXT NOT NUL, claim_status INTEGER, FOREIGN KEY(email) references users(email), FOREIGN KEY(prod_id) references product(prod_id));"""

conn = create_connection(database)
if conn is not None:
    create_table(conn, create_users_table)
    create_table(conn, create_product_table)
    create_table(conn, create_bids_table)
    create_table(conn, create_table_claims)
else:
    print("Error! Cannot create the database connection")

