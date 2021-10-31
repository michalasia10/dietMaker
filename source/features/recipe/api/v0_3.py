from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_pagination import paginate,LimitOffsetPage
import os
from dotenv import load_dotenv


from source.features.recipe.crud import get_all_recipe, delete_recipe, update_recipe, get_recipe_by_id,get_week

from source.core.data.basic_recipe import basic_recipe
from source.core.app.database.get_db import get_db
from source.features.recipe.schema import RecipeWithIngredietns,RecipeInMeal


load_dotenv()
PASSWORD = os.environ.get('REFRESH_PASSWORD')

version = APIRouter(
    prefix="/recipe",
    tags=["recipe"],
)


@version.get('/',
             response_model=LimitOffsetPage[RecipeWithIngredietns])
def get_all(db: Session = Depends(get_db)):
    return paginate(get_all_recipe(db))


# @router.post('/create',
#              status_code=status.HTTP_201_CREATED, )
# def create_new_recipe(request: RecipeBase, db: Session = Depends(get_db)):
#     category = create_recipe(db, request)
#     return category


@version.get('/{recipe_id}',
             response_model=RecipeWithIngredietns)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return get_recipe_by_id(db, recipe_id)


@version.delete('/delete/{recipe_id}')
def delete_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
    return delete_recipe(db, recipe_id)


@version.put('/update/{recipe_id}')
def update_recipe_by_id(request: RecipeWithIngredietns, recipe_id: int, db: Session = Depends(get_db)):
    return update_recipe(db, recipe_id, request)

@version.post('/create_basic/{password}')
def create_basic(password:str,db:Session=Depends(get_db)):
    if password == PASSWORD:
        return basic_recipe(db)

@version.get('in-meal/{recipe_id}', response_model=RecipeInMeal)
def get_meal_by_id(recipe_id: int, db: Session = Depends(get_db)):
    recipe = get_week(db,recipe_id)
    print(recipe.__dict__)
    return recipe