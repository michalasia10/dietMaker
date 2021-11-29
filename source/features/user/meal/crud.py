from sqlalchemy.orm import Session
import json
from datetime import datetime
from source.features.user.meal.models import Meal
from source.features.user.account.models import User
from source.features.user.week.models import DailyMealPlan
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
    return user_meals

def get_users_meals_by_timestamp(db:Session,user_id:int,timestamp:int):
    date = datetime.fromtimestamp(datetime.timestamp(datetime.fromtimestamp(timestamp).replace(hour=0,
                                                                                               minute=0,
                                                                                               second=0,
                                                                                               microsecond=0)))
    user_meals = get_by_id(db, User, user_id).first().settings[0].meal_makro

    meals = []
    for meal in user_meals:
        plan = {}
        plan["name"] = meal.name
        plan["day_meals"] = []
        for day in meal.day_meals:
            if day.date == date:
                plan["day_meals"].append(day)

        meals.append(plan)
    return meals
