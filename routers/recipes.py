from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from crud.recipes import get_all_recipie, create_recipe
from db.get_db import get_db
from schemas.recipes import RecipeBase

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
)


@router.get('/',
            response_model=List[RecipeBase])
def get_all(db: Session = Depends(get_db)):
    return get_all_recipie(db)


@router.post('/create',
             status_code=status.HTTP_201_CREATED, )
def create_new_recipe(request: RecipeBase, db: Session = Depends(get_db)):
    category = create_recipe(db, request)
    return category
