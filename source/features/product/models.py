from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.sql.schema import Column, ForeignKey,Table
from sqlalchemy.sql.sqltypes import Integer, String, Float
from sqlalchemy_utils import URLType

from source.core.app.database.db import Base
from source.features.unit.models import association_table_unit_in_productinmeal


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



class ProductInMeal(Base):
    __tablename__ = 'productinmeals'

    id = Column(Integer, primary_key=True, index=True)
    product = relationship("Product", secondary=association_table_product_in_meal, back_populates='product_as_meal')
    daily_meal_id = Column(Integer, ForeignKey('dailymealplans.id'))
    daily_meal = relationship("DailyMealPlan", back_populates='products')
    name = association_proxy('product', 'name')
    unit = relationship("Unit", secondary=association_table_unit_in_productinmeal, back_populates='product_as_meal')
    amount = Column(Float, index=True)