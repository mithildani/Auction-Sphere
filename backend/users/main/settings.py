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

    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
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
