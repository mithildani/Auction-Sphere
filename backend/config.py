import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_USER = os.environ.get("DATABASE_USER", "postgres") 
    SQLALCHEMY_DATABASE_PASS = os.environ.get("DATABASE_PASS", "postgrespw") 
    SQLALCHEMY_DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost") 
    SQLALCHEMY_DATABASE_PORT = os.environ.get("DATABASE_PORT", "55000") 
    SQLALCHEMY_DATABASE_URI = f"postgresql://{SQLALCHEMY_DATABASE_USER}:{SQLALCHEMY_DATABASE_PASS}@{SQLALCHEMY_DATABASE_HOST}:{SQLALCHEMY_DATABASE_PORT}/auctiondb"
    SQLALCHEMY_ECHO = True

    # Mail sender credentials:
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USERNAME = os.environ.get("MAIL_EMAIL_ADDRESS")
    MAIL_PASSWORD = os.environ.get("MAIL_APP_PASSWORD")
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_SUPPRESS_SEND = False
    TESTING = False

    CACHE_REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
    CACHE_REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
    CACHE_REDIS_URL = f'redis://{CACHE_REDIS_HOST}:{CACHE_REDIS_PORT}/0'
    CACHE_TYPE = "redis"
    CACHE_DEFAULT_TIMEOUT = 300



class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

settings = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}