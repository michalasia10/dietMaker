import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.database import Base

TEST_SQLALCHEMY_DATABASE_URL = 'sqlite:///./test_db.db'
engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL,connect_args ={"check_same_thread":False})
TestingSession = sessionmaker(autocommit=False,autoflush=False,bind=engine)

@pytest.fixture(scope='function')
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)