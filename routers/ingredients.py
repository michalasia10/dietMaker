from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from crud.ingredients import create_ingredient, get_all_ingredietns
from db.get_db import get_db
from schemas.ingredients import IngredientCreate, Ingredient

router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
)


@router.get('/',
            response_model=List[Ingredient])
def get_all(db: Session = Depends(get_db)):
    return get_all_ingredietns(db)


@router.post('/create',
             status_code=status.HTTP_201_CREATED, )
def create_new_ingredients(request: IngredientCreate, db: Session = Depends(get_db)):
    ingredient = create_ingredient(db, request)
    return ingredient
