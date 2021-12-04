from typing import List
from sqlalchemy import inspect
from sqlalchemy.orm import Session
import json
from datetime import datetime, timedelta

from source.features.recipe.models import Recipe
from source.features.user.meal.models import Meal
from source.features.user.account.models import User
from source.features.user.week.models import DailyMealPlan
from source.core.db_queries.crud import get_by_id, simple_object_creator, delete


def create_meals(db: Session, request, user_id: int):
    settings_id = get_by_id(db, User, user_id).first().settings[0].id
    return simple_object_creator(db, Meal, **json.loads(request.json()), settings_id=settings_id)


def delete_meal(db: Session, meal_id: int):
    return delete(db, Meal, meal_id)


def get_meal(db: Session, meal_id: int):
    return get_by_id(db, Meal, meal_id).first()


def get_users_meals(db: Session, user_id: int):
    return get_by_id(db, User, user_id).first().settings[0].meal_makro


def calculate_macro(db: Session, recipes_in_meal: list) -> dict:
    macro: dict = {
        'protein': 0,
        'fat': 0,
        'carbo': 0,
        'kcal': 0,
    }
    for recipe_in_meal in recipes_in_meal:
        recipe_id = recipe_in_meal.recipe[0].id
        recipe = get_by_id(db, Recipe, recipe_id).first()
        for ingredient in recipe.ingredients:
            macro['protein'] += ingredient.product[0].protein
            macro['fat'] += ingredient.product[0].fat
            macro['carbo'] += ingredient.product[0].carbo
            macro['kcal'] += ingredient.product[0].kcal
    return macro


def _calculate_macro_for_whole_day(db: Session, days: List[DailyMealPlan]) -> List[DailyMealPlan]:
    days_with_macro: List[DailyMealPlan] = []
    for day in days:
        day.__dict__['macro'] = calculate_macro(db, day.recipes)
        days_with_macro.append(day)
    return days_with_macro


def _check_days(db: Session, days: List[DailyMealPlan], date_list: list) -> List[DailyMealPlan]:
    days_with_macro: list = _calculate_macro_for_whole_day(db, days)
    dates = [date.date for date in days_with_macro]
    for date in date_list:
        if date not in dates:
            days_with_macro.append({"id": 0, "date": date, 'macro': {}})
    return days_with_macro


def get_users_meals_by_timestamp(db: Session, user_id: int, timestamp: int, count: int):
    date = datetime.fromtimestamp(
        datetime.timestamp(datetime.fromtimestamp(timestamp).replace(hour=0, minute=0, second=0, microsecond=0)))
    date_list: list = [date + timedelta(days=day + 1) for day in range(count)]
    date_list.append(date)
    user_meals: list = get_by_id(db, User, user_id).first().settings[0].meal_makro
    filtered_meals = []
    for meal in user_meals:
        meals = {}
        meals['id'] = meal.id
        meals['name'] = meal.name
        days = meal.day_meals.filter(DailyMealPlan.date.in_(date_list)).all()
        meals['day_meals'] = _check_days(db, days, date_list)
        filtered_meals.append(meals)
    return filtered_meals
