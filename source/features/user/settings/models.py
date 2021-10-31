from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Boolean

from source.core.app.database.db import Base


class UserSetting(Base):
    __tablename__ = 'usersettings'

    id = Column(Integer, primary_key=True, index=True)
    number_of_meals = Column(Integer, index=True, default=3)
    pro = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates='settings')
    meal_makro = relationship("Meal", back_populates='settings')