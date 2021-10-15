from sqlalchemy.orm import Session

from models.meal import Ingredient
from .repeated_crud.repetead import get_all_with_own_paginantion


def get_all_ingredietns(db: Session):
    return get_all_with_own_paginantion(db, Ingredient)


