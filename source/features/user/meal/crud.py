from typing import List

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
    user_meals = get_by_id(db, User, user_id).first().settings[0].meal_makro
    for i in user_meals:
        for j in i.day_meals:
            print(j.__dict__)
    return user_meals

def check_days(days:List[DailyMealPlan],date_list:list):

    dates = [date.date for date in days ]
    print('dates',dates)
    for date in date_list:
        if date not in dates:
            days.append({"id":0,"date":date})
    print(days)
    return days



def get_users_meals_by_timestamp(db:Session,user_id:int,timestamp:int,count:int):
    date = datetime.fromtimestamp(datetime.timestamp(datetime.fromtimestamp(timestamp).replace(hour=0,
                                                                                               minute=0,
                                                                                               second=0,
                                                                                               microsecond=0)))
    date_list : list = [date + timedelta(days=day+1) for day in range(count)]
    date_list.append(date)
    print(date_list)
    user_seetings = get_by_id(db,User,user_id).first().settings[0].meal_makro
    meal_l = []
    for meal in user_seetings:
        meals = {}
        meals['id']=meal.id
        meals['name']=meal.name
        days = meal.day_meals.filter(DailyMealPlan.date.in_(date_list)).all()
        meals['day_meals'] = check_days(days,date_list)
        meal_l.append(meals)
    print(meal_l)
    return meal_l
