from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey,Table
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy_utils import URLType

from source.core.app.database.db import Base


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

class RecipeInMeal(Base):
    __tablename__ = 'recipeinmeals'

    id = Column(Integer, primary_key=True, index=True)
    recipe = relationship("Recipe", secondary=association_table_recipe_in_meal, back_populates='recipe_in_meal')
    daily_meal_id = Column(Integer, ForeignKey('dailymealplans.id'))
    daily_meal = relationship('DailyMealPlan', back_populates='recipes')