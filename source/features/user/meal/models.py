from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float

from source.core.app.database.db import Base

class Meal(Base):
    __tablename__ = 'meals'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    settings_id = Column(Integer, ForeignKey('usersettings.id'))
    settings = relationship("UserSetting", back_populates='meal_makro')
    usermacro = relationship("UserMealMacro", back_populates='meal')
    day_meals = relationship("DailyMealPlan", back_populates='meal',lazy='dynamic')


class UserMealMacro(Base):
    __tablename__ = 'usermealmacros'

    id = Column(Integer, primary_key=True, index=True)
    meal_id = Column(Integer, ForeignKey('meals.id'))
    meal = relationship("Meal", back_populates='usermacro')

    protein = Column(Float, index=True)
    carbo = Column(Float, index=True)
    fat = Column(Float, index=True)
    kcal = Column(Float, index=True)