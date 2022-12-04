# Getting Started with the backend

## Users Microservice

### Pre-requisites
- Python 3
- Pip

### Steps to run Users Microservice Locally
- Create a virtual environment
```shell script
cd backend
python3 -m venv venv
``` 
- Activate the virtual environment
```shell script
venv/bin/activate
```
- Install required Python packages
```shell script
pip3 install -r requirements.txt
```
- Initialize the database
```shell script
flask --app userms db init
```
- Run the migration
```shell script
flask --app userms db upgrade
```
- Run the microservice
```shell script
flask --app userms run
```

### References
- https://flask.palletsprojects.com/en/2.2.x/quickstart/
- https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment
