import json

from sqlalchemy.orm import Session

from models.meal import Ingredient, Unit, Product
from .repeated_crud.repetead import get_all, simple_object_creator, check_exist_by_name, get_by_id


def get_all_ingredietns(db: Session):
    return get_all(db, Ingredient)


def create_ingredient(db: Session, request):
    requestAsDict : dict = json.loads(request.json())
    unitName = requestAsDict.pop('unit')
    product_id = requestAsDict.pop('product_id')
    ingredient_id = simple_object_creator(db,Ingredient,**requestAsDict).id
    ingredient = get_by_id(db,Ingredient,ingredient_id).first()
    unit = check_exist_by_name(db,Unit,{"name":unitName}).first()
    product = get_by_id(db,Product,product_id).first()
    print(unit)
    ingredient.unit.append(unit)
    ingredient.product.append(product)
    print(ingredient)
    db.commit()
    return ingredient
