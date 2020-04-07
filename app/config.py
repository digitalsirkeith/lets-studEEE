from os import getenv

class Config:
    DEBUG = False
    TESTING = False

    USER            = getenv('USER')
    SECRET_KEY      = getenv('SECRET_KEY')
    DATABASE_NAME   = getenv('DATABASE_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{SECRET_KEY}@localhost/{DATABASE_NAME}'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv(f'DATABASE_URL')

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
