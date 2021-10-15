from typing import List

from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session


from crud.users import create_user,delete_user,get_user

from models.user import User
from db.get_db import get_db
from schemas.users import UserBase

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_new_user(request: UserBase, db: Session = Depends(get_db)):
    return create_user(db, request)


@router.get('/{user_id}', response_model=UserBase)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)


@router.delete('/delete/{user_id}')
def delete_users(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)


