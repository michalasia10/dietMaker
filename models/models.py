import enum

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, Enum
from sqlalchemy_utils import URLType

from db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, index=True, unique=True)
    pict_url = Column(URLType, index=True, )

    recipes = relationship("Recipe", back_populates='category')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True,unique=True)
    pict_url = Column(URLType, index=True)
    protein = Column(Float, index=True)
    carbo = Column(Float, index=True)
    fat = Column(Float,index=True)
    description = Column(String,index=True)

    product_as_ingredients = relationship("Ingredient", back_populates='product', uselist=False)

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
    product = relationship("Product", back_populates='product_as_ingredients')
    name = association_proxy('product', 'name')
    amount = Column(Integer, index=True)
    unit = Column(Enum(Units))


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    pict_url = Column(URLType, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates='recipes')
    ingredients = relationship("Ingredient", back_populates='recipe')
    protein = Column(Float, index=True, default=0)
    carbo = Column(Float, index=True, default=0)
    fat = Column(Float, index=True, default=0)
    description = Column(String, index=True, default=0, )
