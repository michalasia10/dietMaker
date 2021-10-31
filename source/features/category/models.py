from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy_utils import URLType

from source.core.app.database.db import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    pict_url = Column(URLType, index=True, )

    recipes = relationship("Recipe", back_populates='category')