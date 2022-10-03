from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def create_connection(db_file):
  conn = None
  conn = sqlite3.connect(db_file)
  return conn

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