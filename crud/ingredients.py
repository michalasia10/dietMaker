from sqlalchemy.orm import Session

from models.meal import Ingredient
from .repeated_crud.repetead import get_all


def get_all_ingredietns(db: Session):
    return get_all(db, Ingredient)


