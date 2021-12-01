from typing import List
from sqlalchemy import inspect
from sqlalchemy.orm import Session
import json
from datetime import datetime,timedelta
from source.features.user.meal.models import Meal
from source.features.user.account.models import User
from source.features.user.week.models import DailyMealPlan
from source.features.user.settings.models import UserSetting
from source.core.db_queries.crud import get_by_id, simple_object_creator, delete



def create_meals(db:Session,request,user_id:int):
    settings_id = get_by_id(db, User, user_id).first().settings[0].id
    return simple_object_creator(db,Meal,**json.loads(request.json()),settings_id=settings_id)

def delete_meal(db:Session,meal_id:int):
    return delete(db,Meal,meal_id)

def get_meal(db:Session,meal_id:int):
    return get_by_id(db,Meal,meal_id).first()

def get_users_meals(db:Session,user_id:int):
    return get_by_id(db, User, user_id).first().settings[0].meal_makro

def _check_days(days:List[DailyMealPlan],date_list:list):
    dates = [date.date for date in days ]
    for date in date_list:
        if date not in dates:
            days.append({"id":0,"date":date})
    return days


def get_users_meals_by_timestamp(db:Session,user_id:int,timestamp:int,count:int):
    print("dupa",timestamp)
    date  = datetime.fromtimestamp(datetime.timestamp(datetime.fromtimestamp(timestamp).replace(hour=0, minute=0,second=0,microsecond=0)))
    date_list : list = [date + timedelta(days=day+1) for day in range(count)]
    date_list.append(date)
    user_meals : list = get_by_id(db, User, user_id).first().settings[0].meal_makro
    filtered_meals = []
    for meal in user_meals:
        meals = {}
        meals['id']=meal.id
        meals['name']=meal.name
        days = meal.day_meals.filter(DailyMealPlan.date.in_(date_list)).all()
        meals['day_meals'] = _check_days(days, date_list)
        filtered_meals.append(meals)
    return filtered_meals
