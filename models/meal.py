import datetime

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer, String, Float, TIMESTAMP
from sqlalchemy_utils import URLType

from db.database import Base


class DailyMealPlan(Base):
    __tablename__ = 'dailymealplans'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(TIMESTAMP, default=datetime.datetime.now().timestamp(), index=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates='day_meals')
    recipes = relationship("RecipeInMeal", back_populates='daily_meal')
    products = relationship("ProductInMeal", back_populates='daily_meal')


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    pict_url = Column(URLType, index=True, )

    recipes = relationship("Recipe", back_populates='category')


association_table_tags = Table("association_table_tags", Base.metadata,
                               Column("product_id", ForeignKey('products.id'), primary_key=True),
                               Column('tag_id', ForeignKey('tags.id'), primary_key=True)
                               )


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    product = relationship('Product', secondary=association_table_tags, back_populates='tags')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer, index=True, unique=True)
    name = Column(String, index=True)
    pict_url = Column(URLType, index=True)
    protein = Column(Float, index=True)
    carbo = Column(Float, index=True)
    fat = Column(Float, index=True)
    kcal = Column(Float, index=True)
    description = Column(String, index=True, default='')

    tags = relationship('Tag', secondary=association_table_tags, back_populates='product')
    product_as_ingredients = relationship("Ingredient", back_populates='product', uselist=False)
    product_as_meal = relationship("ProductInMeal", back_populates='product')


class Unit(Base):
    __tablename__ = 'units'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    ingreditens = relationship("Ingredient", back_populates='unit')
    product_as_meal = relationship("ProductInMeal", back_populates='unit')


class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship("Recipe", back_populates='ingredients')
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", back_populates='product_as_ingredients')
    name = association_proxy('product', 'name')
    unit_id = Column(Integer, ForeignKey('units.id'))
    unit = relationship("Unit", back_populates='ingreditens')
    amount = Column(Float, index=True)


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates='recipes')
    name = Column(String, index=True, unique=True)
    pict_url = Column(URLType, index=True)
    ingredients = relationship("Ingredient", back_populates='recipe')
    description = Column(String, index=True, default='', )

    recipe_in_meal = relationship("RecipeInMeal", back_populates='recipe')


class ProductInMeal(Base):
    __tablename__ = 'productinmeals'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", back_populates='product_as_meal')
    daily_meal_id = Column(Integer, ForeignKey('dailymealplans.id'))
    daily_meal = relationship("DailyMealPlan", back_populates='products')
    name = association_proxy('product', 'name')
    unit_id = Column(Integer, ForeignKey('units.id'))
    unit = relationship("Unit", back_populates='product_as_meal')
    amount = Column(Float, index=True)


class RecipeInMeal(Base):
    __tablename__ = 'recipeinmeals'

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship("Recipe", back_populates='recipe_in_meal')
    daily_meal_id = Column(Integer, ForeignKey('dailymealplans.id'))
    daily_meal = relationship('DailyMealPlan', back_populates='recipes')
