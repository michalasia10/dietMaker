from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE = 'sqllite:///./diet.db'

engine = create_engine(SQLALCHEMY_DATABASE,connect_args = {"check_same_thread":False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)
