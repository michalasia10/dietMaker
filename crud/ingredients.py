import json

from sqlalchemy.orm import Session

from models.meal import Ingredient
from .repeated_crud.repetead import get_all, simple_object_creator


def get_all_ingredietns(db: Session):
    return get_all(db, Ingredient)


def create_ingredient(db: Session, request):
    requestAsDict = json.loads(request.json())
    return simple_object_creator(db, Ingredient, **requestAsDict)
