from sqlalchemy.orm import Session

from models.meal import Recipe
from .repeated_crud.repetead import get_all_with_lib_paginantion, get_by_id_with_valid, delete, update


def get_all_recipe(db: Session):
    return get_all_with_lib_paginantion(db, Recipe)


def get_recipe_by_id(db: Session, recipe_id: int):
    return get_by_id_with_valid(db, Recipe, recipe_id).first()


# def create_recipe(db: Session, request):
#     return create(db, Recipe, request)


def delete_recipe(db: Session, recipe_id: int):
    recipe = get_recipe_by_id(db, recipe_id)
    recipe.ingredients = []
    db.commit()
    return delete(db, Recipe, recipe_id)


def update_recipe(db: Session, recipe_id: int, request):
    return update(db, Recipe, recipe_id, request)
