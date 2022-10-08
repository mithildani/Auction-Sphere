# Getting Started with Flask Locally

### Before we start the Python project, we will create a virtual environment
Windows: `py -3 -m venv venv`
Mac: `python3 -m venv venv`

### Activate the virtual env
Windows: `venv\Scripts\activate` 
Mac: `venv/bin/activate`  
 
 **if permission denied error, try the below** 
 
 `. venv/bin/activate`
 or
 `source venv/bin/activate`

### Install requirements
Windows: `pip install -e .`
Mac: `pip3 install -e .`

### To run project
`flask --app app run`


### Reference-
https://flask.palletsprojects.com/en/2.2.x/quickstart/ <br />
https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment
