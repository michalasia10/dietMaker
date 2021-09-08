from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,index=True,unique=True)
    pict_url = Column(String,index=True)

    products = relationship("Product",back_populates='category')


class Product(Base):

    __tabelname__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True,unique=True)
    pict_url = Column(String, index=True)
    protein = Column(Float)
    carbo =Column(Float)
    fat = Column(Float)

    category_id = Column(Integer,ForeignKey('categories.id'))
    category = relationship("Categpry",back_populates = 'products')

