import json

from sqlalchemy.orm import Session

from source.core.db_queries.crud import check_exist_by_name, simple_object_creator,get_by_id
from source.features.product.models import Product
from source.features.ingredient.models import Ingredient
from source.features.unit.models import Unit
from source.features.recipe.models import Recipe



def basic_recipe(db:Session,jsonPath = 'recipies.json'):
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


