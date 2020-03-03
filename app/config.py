from dotenv import load_dotenv
load_dotenv()
from os import getenv

environment = getenv('FLASK_ENV')
if environment is None:
    raise KeyError

if environment == 'development':
    environment = 'DEV'
elif environment == 'production':
    environment = 'PROD'
else:
    raise KeyError

USER            = getenv(f'{environment}_USER')
SECRET_KEY      = getenv(f'{environment}_SECRET_KEY')

if environment == 'DEV':
    DATABASE_URI    = f'postgresql://{USER}:{SECRET_KEY}@localhost'
else:
    DATABASE_URI    = getenv(f'{environment}_DATABASE_URI')

if __name__ == '__main__':
    print(f'USER: {USER}')
    print(f'SECRET_KEY: {SECRET_KEY}')
    print(f'DATABASE_URI: {DATABASE_URI}')