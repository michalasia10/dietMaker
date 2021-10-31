from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session


from source.features.user.account.crud import create_user,delete_user,get_user

from source.core.app.database.get_db import get_db
from source.features.user.account.schema import UserBase

version = APIRouter(
    prefix="/user",
    tags=["user"],
)


@version.post('/create', status_code=status.HTTP_201_CREATED)
def create_new_user(request: UserBase, db: Session = Depends(get_db)):
    return create_user(db, request)


@version.get('/{user_id}', response_model=UserBase)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)


@version.delete('/delete/{user_id}')
def delete_users(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)


