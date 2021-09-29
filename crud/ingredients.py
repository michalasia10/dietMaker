from sqlalchemy.orm import Session

from sqlalchemy.orm import Session

from models.meal import Ingredient
from .repeated_crud.repetead import get_all, create


def get_all_ingredietns(db: Session):
    return get_all(db, Ingredient)


def create_ingredient(db: Session, request):
    return create(db, Ingredient, request)
