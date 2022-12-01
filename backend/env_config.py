import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_ECHO = True

    # Mail sender credentials:
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_EMAIL_ADDRESS = os.environ.get("MAIL_EMAIL_ADDRESS")
    MAIL_APP_PASSWORD = os.environ.get("MAIL_APP_PASSWORD")

    REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
    REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
    
