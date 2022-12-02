import os


class Config:
    BASE_DIR = os.path.join(os.pardir, os.path.dirname(__file__))
    SECRET_KEY = "abcd"

    DEBUG = False
    TESTING = False
    PORT = 8000


class DevelopmentConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "development")
    DEBUG = True
    ASSETS_DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_USER = os.environ.get("DATABASE_USER", "postgres") 
    SQLALCHEMY_DATABASE_PASS = os.environ.get("DATABASE_PASS", "postgrespw") 
    SQLALCHEMY_DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost") 
    SQLALCHEMY_DATABASE_PORT = os.environ.get("DATABASE_PORT", "55000") 
    SQLALCHEMY_DATABASE_URI = f"postgresql://{SQLALCHEMY_DATABASE_USER}:{SQLALCHEMY_DATABASE_PASS}@{SQLALCHEMY_DATABASE_HOST}:{SQLALCHEMY_DATABASE_PORT}/auctiondb"
    SQLALCHEMY_ENGINE_OPTIONS = {
        'case_sensitive': False,
        'echo': True,
        'echo_pool': True
    }


class TestingConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "testing")
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = False
    USE_RELOADER = False


settings = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
