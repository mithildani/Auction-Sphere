import os

class Config(object):
    # Mail sender credentials:
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_EMAIL_ADDRESS = os.environ.get("MAIL_EMAIL_ADDRESS")
    MAIL_APP_PASSWORD = os.environ.get("MAIL_APP_PASSWORD")
