from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, Boolean

from db.database import Base


class Meal(Base):
    __tablename__ = 'meals'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    settings_id = Column(Integer, ForeignKey('usersettings.id'))
    settings = relationship("UserSetting", back_populates='makro')
    usermacro = relationship("UserMealMacro", back_populates='meal')
    day_meals = relationship("DailyMealPlan", back_populates='meal')



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    settings = relationship("UserSetting", back_populates='user')



class UserSetting(Base):
    __tablename__ = 'usersettings'

    id = Column(Integer, primary_key=True, index=True)
    number_of_meals = Column(Integer, index=True, default=3)
    pro = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates='settings')
    meal_makro = relationship("Meal", back_populates='settings')


class UserMealMacro(Base):
    __tablename__ = 'usermealmacros'

    id = Column(Integer, primary_key=True, index=True)
    meal_id = Column(Integer, ForeignKey('meals.id'))
    meal = relationship("Meal", back_populates='usermacro')

    protein = Column(Float, index=True)
    carbo = Column(Float, index=True)
    fat = Column(Float, index=True)
    kcal = Column(Float, index=True)
