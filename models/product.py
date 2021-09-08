from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer,String,Float
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship
from db.database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True,unique=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates='products')
    pict_url = Column(URLType, index=True)
    protein = Column(Float, index=True)
    carbo = Column(Float, index=True)
    fat = Column(Float,index=True)
    description = Column(String,index=True)

    product_as_ingredients = relationship("Ingredient", back_populates='product')