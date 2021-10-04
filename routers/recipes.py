from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.recipes import get_all_recipie, delete_recipe, update_recipe, get_recipe_by_id
from data.basic_recipe import basic_recipe
from db.get_db import get_db
from schemas.recipes import RecipeWithIngredietns

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"],
)


@router.get('/',
            response_model=List[RecipeWithIngredietns])
def get_all(db: Session = Depends(get_db)):
    return get_all_recipie(db)


# @router.post('/create',
#              status_code=status.HTTP_201_CREATED, )
# def create_new_recipe(request: RecipeBase, db: Session = Depends(get_db)):
#     category = create_recipe(db, request)
#     return category


@router.get('/{recipe_id}',
            response_model=RecipeWithIngredietns)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return get_recipe_by_id(db, recipe_id)


@router.delete('/delete/{recipe_id}')
def delete_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
    return delete_recipe(db, recipe_id)


@router.put('/update/{recipe_id}')
def update_recipe_by_id(request: RecipeWithIngredietns, recipe_id: int, db: Session = Depends(get_db)):
    return update_recipe(db, recipe_id, request)

@router.post('/create_basic/{password}')
def create_basic(password:str,db:Session=Depends(get_db)):
    if password == 'michu':
        return basic_recipe(db)