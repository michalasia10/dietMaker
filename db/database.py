import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from distutils.util import strtobool

# local
# SQLALCHEMY_DATABASE_URL = "sqlite:///./diet.db"

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


engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
