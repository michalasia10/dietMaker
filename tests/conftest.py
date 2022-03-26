import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from source.core.app.database.db import Base

TEST_SQLALCHEMY_DATABASE_URL = 'sqlite:///./test_db.db'
engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL,connect_args ={"check_same_thread":False})
TestingSession = sessionmaker(autocommit=False,autoflush=False,bind=engine)
# Base = declarative_base()

@pytest.fixture(scope='function',autouse=True)
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)