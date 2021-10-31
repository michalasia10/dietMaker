from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session


from source.features.user.meal.crud import create_meals,delete_meal,get_meal

from source.core.app.database.get_db import get_db
from source.features.user.meal.schema import UserMeals

version = APIRouter(
    prefix="/usermeals",
    tags=["usermeals"],
)


@version.post('/create/{settings_id}', status_code=status.HTTP_201_CREATED)
def create_new_product(settings_id:int,request: UserMeals, db: Session = Depends(get_db)):
    return create_meals(db, request,settings_id)


@version.get('/{meal_id}', response_model=UserMeals)
def get_product_by_id(meal_id: int, db: Session = Depends(get_db)):
    return get_meal(db, meal_id)


@version.delete('/delete/{meal_id}')
def delete_products(meal_id: int, db: Session = Depends(get_db)):
    return delete_meal(db, meal_id)
