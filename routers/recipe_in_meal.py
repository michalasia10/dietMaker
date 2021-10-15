from typing import List

from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session


from crud.recipe_in_meal import get_week

from db.get_db import get_db
from schemas.recipe_in_meal import RecipeInMeal

router = APIRouter(
    prefix="/recipeinmeal",
    tags=["recipeinmeal"],
)


@router.get('/{recipe_id}', response_model=RecipeInMeal)
def get_meal_by_id(recipe_id: int, db: Session = Depends(get_db)):
    recipe = get_week(db,recipe_id)
    print(recipe.__dict__)
    return recipe