from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.ingredients import get_all_ingredietns
from db.get_db import get_db
from schemas.ingredients import Ingredient

router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
)


@router.get('/',
            response_model=List[Ingredient])
def get_all(db: Session = Depends(get_db)):
    return get_all_ingredietns(db)


