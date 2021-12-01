from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from typing import List

from source.features.user.meal.crud import create_meals,delete_meal,\
    get_meal,get_users_meals,get_users_meals_by_timestamp

from source.core.app.database.get_db import get_db
from source.features.user.meal.schema import UserMealBasic, UserMeals, UserMealsWithoutQUery
from source.features.user.week.api.v0_3 import plan


version = APIRouter(
    prefix="/usermeals",
    tags=["usermeals"],
)


@version.post('/create/{user_id}', status_code=status.HTTP_201_CREATED)
def create_new_product(settings_id:int, request: UserMealBasic, db: Session = Depends(get_db)):
    return create_meals(db, request,settings_id)


@version.get('/{meal_id}')
def get_product_by_id(meal_id: int, db: Session = Depends(get_db)):
    return get_meal(db, meal_id)


@version.delete('/delete/{meal_id}')
def delete_products(meal_id: int, db: Session = Depends(get_db)):
    return delete_meal(db, meal_id)

@plan.get('/{user_id}',response_model=List[UserMeals])
def get_all_user_meals(user_id: int, db: Session = Depends(get_db)):
    sth = get_users_meals(db,user_id)
    return sth
