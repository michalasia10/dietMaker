import json

from sqlalchemy.orm import Session

from crud.repeated_crud.repetead import simple_object_creator, check_exist_by_name, get_by_id
from models.meal import Ingredient, Unit, Product, Recipe


def basic_recipe(db:Session,jsonPath = 'data/recipies.json'):
    jsonFile : list = json.load(open(jsonPath))
    for recipe  in jsonFile:
        ingredients = recipe.pop('ingredients')
        recipe_id = simple_object_creator(db,Recipe,**recipe).id
        for ingredient in ingredients:
            amount = ingredient.pop('amount')
            ingredientObject_id = simple_object_creator(db, Ingredient, recipe_id=recipe_id,amount=amount).id
            ingredientObject = get_by_id(db, Ingredient, ingredientObject_id).first()
            unitName = ingredient.pop('unit')
            unit = check_exist_by_name(db, Unit, {"name": unitName}).first()
            product_id = ingredient.pop('product_id')
            product = get_by_id(db, Product, product_id).first()
            ingredientObject.unit.append(unit)
            ingredientObject.product.append(product)
            db.commit()
            print(get_by_id(db,Recipe,recipe_id).first(),'created')


