import json

from sqlalchemy.orm import Session

from models.models import Ingredient, Recipe, Product
from .repeated_crud.repetead import get_by_id_with_valid, get_all, create_with_relation, update


def get_all_ingredietns(db: Session):
    return get_all(db, Ingredient)


def create_ingredient(db: Session, request):
    requestAsDict = json.loads(request.json())
    product_id = requestAsDict['product_id']
    product = get_by_id_with_valid(db, Product, product_id).first().__dict__
    productMakros = {makroKey: product[makroKey] for makroKey in product if makroKey in ('carbo', 'fat', 'protein')}

    recipe_id = requestAsDict['recipe_id']
    recipe = get_by_id_with_valid(db, Recipe, recipe_id).first().__dict__
    oldRecipeMakros = {makroKey: recipe[makroKey] for makroKey in recipe if makroKey in ('carbo', 'fat', 'protein')}
    oldRecipeMakros.update(productMakros)

    update(db, Recipe, recipe_id, oldRecipeMakros)
    return create_with_relation(db, Ingredient, request)
