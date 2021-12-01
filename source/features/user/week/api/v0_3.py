import json
from typing import List

from fastapi import APIRouter, Depends,status
from pydantic import ValidationError
from sqlalchemy.orm import Session
from starlette.requests import Request

from source.features.user.meal.schema import UserMeals, UserMealsWithoutQUery
from source.features.user.week.crud import add_recipe,get_all_week,get_week,delete_week,delete_recipe_from_week
from source.features.user.meal.crud import get_users_meals_by_timestamp
from source.core.app.database.get_db import get_db
from source.features.user.week.schema import UserWeek

version = APIRouter(
    prefix="/userweek",
    tags=["userweek"],
)

plan = APIRouter(
    prefix="/plan",
    tags=["plan"],
)
@version.get('/',
             response_model=List[UserWeek])
def get_all(db: Session = Depends(get_db)):
    return get_all_week(db)

@plan.post('/{timestamp}/{meal_id}/{recipe_id}', status_code=status.HTTP_201_CREATED)
def add_recipe_to_plan(timestamp:int,meal_id:int,recipe_id:int, db: Session = Depends(get_db)):
    return add_recipe(db,timestamp,meal_id,recipe_id)

@plan.get('/{user_id}/{timestamp}/{count}',response_model=List[UserMealsWithoutQUery])
def get_user_meals_by_timestamp_with_count(user_id : int, timestamp:int, count : int,db : Session=Depends(get_db)):
    return get_users_meals_by_timestamp(db,user_id,timestamp,count)

@version.get('/{week_id}', response_model=UserWeek)
def get_week_by_id(week_id: int, db: Session = Depends(get_db)):
    return get_week(db, week_id)

@version.delete('/delete/{week_id}', response_model=UserWeek)
def get_delete_by_id(week_id: int, db: Session = Depends(get_db)):
    return delete_week(db, week_id)


@version.delete('/delete/{week_id}/{recipe_id}',status_code=status.HTTP_200_OK)
def delete_recipe_week(week_id:int,recipe_id:int,db:Session=Depends(get_db)):
    return delete_recipe_from_week(db,week_id,recipe_id)

