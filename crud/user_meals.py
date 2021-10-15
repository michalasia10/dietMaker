from sqlalchemy.orm import Session
import json
from models.user import Meal
from .repeated_crud.repetead import get_by_id, simple_object_creator, get_all_with_lib_paginantion, delete

def create_meals(db:Session,request,settings_id:int):
    return simple_object_creator(db,Meal,**json.loads(request.json()),settings_id=settings_id)

def delete_meal(db:Session,meal_id:int):
    return delete(db,Meal,meal_id)

def get_meal(db:Session,meal_id:int):
    return get_by_id(db,Meal,meal_id).first()