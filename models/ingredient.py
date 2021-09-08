from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer,Enum
from sqlalchemy.orm import relationship
from db.database import Base
import enum


class Units(str,enum.Enum):
    l = 'liter'
    ml = 'mililiter'
    g = 'gram'
    kg = 'kilogram'
    dg = 'decagram'


class Ingredient(Base):
    __tablename__ = 'ingredtiens'
    id = Column(Integer,primary_key=True,index=True)
    recipe_id = Column(Integer,ForeignKey('recipes.id'))
    recipe = relationship("Recipe",back_populates='ingredients')
    product_id = Column(Integer,ForeignKey('products.id'))
    product = relationship("Product",back_populates='product_as_ingredients')
    amount = Column(Integer,index=True)
    unit = Column(Enum(Units))
