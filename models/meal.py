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
    date = Column(TIMESTAMP, default=datetime.datetime.now().timestamp(), index=True)
    meal_id = Column(Integer, ForeignKey('meals.id'))
    meal = relationship("Meal", back_populates='day_meals')
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


association_table_product_ingredient = Table("association_table_product_ingredient", Base.metadata,
                                             Column("ingredient_id", ForeignKey('ingredients.id'), primary_key=True),
                                             Column('product_id', ForeignKey('products.id'), primary_key=True)
                                             )

association_table_product_in_meal = Table("association_table_product_in_meal", Base.metadata,
                                          Column("productinmeal_id", ForeignKey('productinmeals.id'), primary_key=True),
                                          Column('product_id', ForeignKey('products.id'), primary_key=True)
                                          )


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
    product_as_ingredients = relationship("Ingredient", secondary=association_table_product_ingredient,
                                          back_populates='product', uselist=False)
    product_as_meal = relationship("ProductInMeal", secondary=association_table_product_in_meal,
                                   back_populates='product')


association_table_unit_in_ingredient = Table("association_table_unit_in_ingredient", Base.metadata,
                                             Column("ingredient_id", ForeignKey('ingredients.id'), primary_key=True),
                                             Column('unit_id', ForeignKey('units.id'), primary_key=True)
                                             )

association_table_unit_in_productinmeal = Table("association_table_unit_in_productinmeal", Base.metadata,
                                                Column("productinmeal_id", ForeignKey('productinmeals.id'),
                                                       primary_key=True),
                                                Column('unit_id', ForeignKey('units.id'), primary_key=True)
                                                )


class Unit(Base):
    __tablename__ = 'units'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    ingreditens = relationship("Ingredient", secondary=association_table_unit_in_ingredient, back_populates='unit')
    product_as_meal = relationship("ProductInMeal", secondary=association_table_unit_in_productinmeal,
                                   back_populates='unit')


class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship("Recipe", back_populates='ingredients')
    product = relationship("Product", secondary=association_table_product_ingredient,
                           back_populates='product_as_ingredients')
    name = association_proxy('product', 'name')
    unit = relationship("Unit", secondary=association_table_unit_in_ingredient, back_populates='ingreditens')
    amount = Column(Float, index=True)


association_table_recipe_in_meal = Table("association_table_recipe_in_meal", Base.metadata,
                                         Column("recipeinmeal_id", ForeignKey('recipeinmeals.id'), primary_key=True),
                                         Column('recipe_id', ForeignKey('recipes.id'), primary_key=True)
                                         )


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates='recipes')
    name = Column(String, index=True, unique=True)
    pict_url = Column(URLType, index=True)
    ingredients = relationship("Ingredient", back_populates='recipe')
    description = Column(String, index=True, default='', )

    recipe_in_meal = relationship("RecipeInMeal", secondary=association_table_recipe_in_meal, back_populates='recipe')


class ProductInMeal(Base):
    __tablename__ = 'productinmeals'

    id = Column(Integer, primary_key=True, index=True)
    product = relationship("Product", secondary=association_table_product_in_meal, back_populates='product_as_meal')
    daily_meal_id = Column(Integer, ForeignKey('dailymealplans.id'))
    daily_meal = relationship("DailyMealPlan", back_populates='products')
    name = association_proxy('product', 'name')
    unit = relationship("Unit", secondary=association_table_unit_in_productinmeal, back_populates='product_as_meal')
    amount = Column(Float, index=True)


class RecipeInMeal(Base):
    __tablename__ = 'recipeinmeals'

    id = Column(Integer, primary_key=True, index=True)
    recipe = relationship("Recipe", secondary=association_table_recipe_in_meal, back_populates='recipe_in_meal')
    daily_meal_id = Column(Integer, ForeignKey('dailymealplans.id'))
    daily_meal = relationship('DailyMealPlan', back_populates='recipes')
