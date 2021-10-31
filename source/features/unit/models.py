from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey,Table
from sqlalchemy.sql.sqltypes import Integer, String

from source.core.app.database.db import Base


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