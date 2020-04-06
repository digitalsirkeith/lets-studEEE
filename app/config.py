from dotenv import load_dotenv
load_dotenv()
from os import getenv

environment = getenv('FLASK_ENV')
if environment is None:
    raise KeyError

USER            = getenv('USER')
SECRET_KEY      = getenv('SECRET_KEY')
DATABASE_NAME   = getenv('DATABASE_NAME')

if environment == 'development':
    DATABASE_URI    = f'postgresql://{USER}:{SECRET_KEY}@localhost/{DATABASE_NAME}'
else:
    DATABASE_URI    = getenv(f'DATABASE_URL')

if __name__ == '__main__':
    print(f'USER: {USER}')
    print(f'SECRET_KEY: {SECRET_KEY}')
    print(f'DATABASE_URI: {DATABASE_URI}')