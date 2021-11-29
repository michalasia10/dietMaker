from sqlalchemy.orm import Session
import json
from source.features.user.account.models import User
from source.features.user.settings.models import UserSetting
from source.core.db_queries.crud  import get_by_id, simple_object_creator, delete

def create_settings(db:Session,request,user_id:int):
    return simple_object_creator(db,UserSetting,**json.loads(request.json()),user_id=user_id)

def delete_settings(db:Session,settings_id:int):
    return delete(db,UserSetting,settings_id)

def get_settings(db:Session,user_id:int):
    settings_id = get_by_id(db,User,user_id).first().settings[0].id
    return get_by_id(db,UserSetting,settings_id).first()