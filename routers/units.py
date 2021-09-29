from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from crud.recipes import get_all_recipie, create_recipe, \
    delete_recipe, get_recipe_by_id
from db.get_db import get_db
from schemas.units import UnitBase

router = APIRouter(
    prefix="/units",
    tags=["units"],
)

@router.get('/',
            response_model=List[UnitBase])
def get_all(db: Session = Depends(get_db)):
    return get_all_recipie(db)


@router.post('/create',
             status_code=status.HTTP_201_CREATED, )
def create_new_recipe(request: UnitBase, db: Session = Depends(get_db)):
    category = create_recipe(db, request)
    return category


@router.get('/{unit_id}',
            response_model=UnitBase)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return get_recipe_by_id(db, recipe_id)


@router.delete('/delete/{unit_id}')
def delete_recipe_by_id(unit_id: int, db: Session = Depends(get_db)):
    return delete_recipe(db, unit_id)
