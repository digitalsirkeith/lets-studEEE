from os import getenv

environment = getenv('FLASK_ENV')
if environment is None:
    raise KeyError

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

if __name__ == '__main__':
    print(f'USER: {USER}')
    print(f'SECRET_KEY: {SECRET_KEY}')
    print(f'DATABASE_URI: {DATABASE_URI}')