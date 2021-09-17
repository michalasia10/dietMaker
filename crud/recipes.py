from sqlalchemy.orm import Session

from models.models import Recipe
from .repeated_crud.repetead import create, get_all


def get_all_recipie(db: Session):
    return get_all(db, Recipe)


def create_recipe(db: Session, request):
    return create(db, Recipe, request)
