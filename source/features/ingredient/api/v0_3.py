from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from source.features.ingredient.crud import get_all_ingredietns
from source.core.app.database.get_db import get_db
from source.features.ingredient.schema import Ingredient

version = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
)

version.get('/',
            response_model=List[Ingredient])
def get_all(db: Session = Depends(get_db)):
    return get_all_ingredietns(db)