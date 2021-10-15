from typing import List

from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session


from crud.users_settings import create_settings,delete_settings,get_settings

from db.get_db import get_db
from schemas.users_settings import UserSettings

router = APIRouter(
    prefix="/settings",
    tags=["settings"],
)


@router.post('/create/{user_id}', status_code=status.HTTP_201_CREATED)
def create_new_settings(user_id:int,request: UserSettings, db: Session = Depends(get_db)):
    return create_settings(db, request,user_id)


@router.get('/{user_id}', response_model=UserSettings)
def get_settings_by_id(user_id: int, db: Session = Depends(get_db)):
    return get_settings(db, user_id)


@router.delete('/delete/{user_id}')
def delete_settings_by_id(user_id: int, db: Session = Depends(get_db)):
    return delete_settings(db, user_id)
