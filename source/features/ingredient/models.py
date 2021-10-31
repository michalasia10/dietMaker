from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float

from source.core.app.database.db import Base
from source.features.product.models import association_table_product_ingredient
from source.features.unit.models import association_table_unit_in_ingredient

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