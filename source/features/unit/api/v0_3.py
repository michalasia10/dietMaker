from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from source.features.unit.crud import get_all_units, get_unit_by_id, create_unit, delete_unit
from source.core.app.database.get_db import get_db
from source.features.unit.schema import UnitBase

version = APIRouter(
    prefix="/units",
    tags=["units"],
)


@version.get('/',
             response_model=List[UnitBase])
def get_all(db: Session = Depends(get_db)):
    return get_all_units(db)


@version.post('/create',
              status_code=status.HTTP_201_CREATED, )
def create_new_recipe(request: UnitBase, db: Session = Depends(get_db)):
    category = create_unit(db, request)
    return category


@version.get('/{unit_id}',
             response_model=UnitBase)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return get_unit_by_id(db, recipe_id)


@version.delete('/delete/{unit_id}')
def delete_recipe_by_id(unit_id: int, db: Session = Depends(get_db)):
    return delete_unit(db, unit_id)
