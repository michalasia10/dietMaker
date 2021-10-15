from sqlalchemy.orm import Session

from models.meal import RecipeInMeal
from .repeated_crud.repetead import get_by_id, create, get_all_with_lib_paginantion, delete


def get_week(db:Session,week_id:int):
    return get_by_id(db,RecipeInMeal,week_id).first()