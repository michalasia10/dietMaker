from sqlalchemy.orm import Session
import json
from models.user import User
from .repeated_crud.repetead import get_by_id, simple_object_creator, get_all_with_lib_paginantion, delete

def create_user(db:Session,request):
    return simple_object_creator(db,User,**json.loads(request.json()))

def delete_user(db:Session,user_id:int):
    return delete(db,User,user_id)

def get_user(db:Session,user_id:int):
    return get_by_id(db,User,user_id)