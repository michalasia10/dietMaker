from sqlalchemy.orm import Session

from models.meal import Unit
from .repeated_crud.repetead import create, get_all, get_by_id_with_valid, delete


def get_all_recipie(db: Session):
    return get_all(db, Unit)

def get_recipe_by_id(db: Session, unit_id: int):
    return get_by_id_with_valid(db, Unit, unit_id).first()


def create_recipe(db: Session, request):
    return create(db, Unit, request)


def delete_recipe(db: Session, recipe_id: int):
    return delete(db, Unit, recipe_id)
