from sqlalchemy.orm import Session
from datetime import datetime
from source.features.recipe.models import RecipeInMeal,Recipe
from source.features.user.meal.crud import get_users_meals
from source.features.user.week.models import DailyMealPlan
from source.core.db_queries.crud  import get_by_id, simple_object_creator, get_all_with_own_paginantion, delete,get_by_atrr

def add_recipe(db:Session,timestamp:int,meal_id:int,recipe_id:int,user_id:int):
    reversed_timestamp = datetime.fromtimestamp(
        datetime.timestamp(
            datetime.fromtimestamp(timestamp).
                replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0)
        )
    )
    dayilyMeal = get_by_atrr(db,DailyMealPlan,"date",reversed_timestamp).first()
    if not dayilyMeal:
        dailyMealId = simple_object_creator(db, DailyMealPlan,
                                            date=reversed_timestamp,
                                            meal_id=meal_id).id
    else:
        dailyMealId = dayilyMeal.id
    recipeInMeal = simple_object_creator(db,RecipeInMeal,daily_meal_id = dailyMealId)
    recipe = get_by_id(db,Recipe,recipe_id).first()
    recipeInMeal.recipe.append(recipe)
    db.commit()
    return get_users_meals(db,user_id)


def delete_week(db:Session,week_id:int):
    return delete(db, DailyMealPlan, week_id)
#
def get_week(db:Session,week_id:int):
    return get_by_id(db,DailyMealPlan,week_id).first()

def delete_recipe_from_week(db:Session,week_id:int,recipe_id):
    week = get_by_id(db, DailyMealPlan, week_id).first()
    recipe = get_by_id(db,RecipeInMeal,recipe_id).first()
    week.recipes.remove(recipe)
    db.commit()
    print('Deleted')

def get_all_week(db:Session):
    data = get_all_with_own_paginantion(db, DailyMealPlan)
    return data