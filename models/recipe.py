from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship
from db.database import Base


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,index=True,unique=True)
    pict_url = Column(URLType,index=True)
    ingredients = relationship("Ingredient",back_populates='recipe')