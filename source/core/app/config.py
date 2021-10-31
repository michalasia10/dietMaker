import os
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv()

DEBUG  = strtobool(os.environ.get('DEBUG'))

SQLALCHEMY_DATABASE_URL = ''

if DEBUG:
    DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_HOSTNAME = os.environ.get("DATABASE_HOSTNAME")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}/{DATABASE_NAME}"
else:
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)


APP_NAME = 'dietMaker'
SERVER_ADRESS = "0.0.0.0"
SERVER_PORT = "${PORT:-5000}"