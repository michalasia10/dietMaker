import datetime

from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, TIMESTAMP

from source.core.app.database.db import Base

class DailyMealPlan(Base):
    __tablename__ = 'dailymealplans'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(TIMESTAMP, default=datetime.datetime.now().timestamp(), index=True)
    meal_id = Column(Integer, ForeignKey('meals.id'))
    meal = relationship("Meal", back_populates='day_meals')
    recipes = relationship("RecipeInMeal", back_populates='daily_meal')
    products = relationship("ProductInMeal", back_populates='daily_meal')