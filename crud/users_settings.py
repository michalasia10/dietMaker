from sqlalchemy.orm import Session
import json
from models.user import UserSetting
from .repeated_crud.repetead import get_by_id, simple_object_creator, get_all_with_lib_paginantion, delete

def create_settings(db:Session,request,user_id:int):
    return simple_object_creator(db,UserSetting,**json.loads(request.json()),user_id=user_id)

def delete_settings(db:Session,settings_id:int):
    return delete(db,UserSetting,settings_id)

def get_settings(db:Session,settings_id:int):
    return get_by_id(db,UserSetting,settings_id)