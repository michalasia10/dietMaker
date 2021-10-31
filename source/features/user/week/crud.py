from sqlalchemy.orm import Session
from datetime import datetime
from source.features.recipe.models import RecipeInMeal,Recipe
from source.features.user.week.models import DailyMealPlan
from source.core.db_queries.crud  import get_by_id, simple_object_creator, get_all_with_own_paginantion, delete

def create_week(db:Session,timestamp:int,meal_id:int,recipe_id:int):
    newTimestamp = datetime.fromtimestamp(datetime.timestamp(datetime.fromtimestamp(timestamp).replace(hour=0,minute=0,second=0,microsecond=0)))
    dailyMealId = simple_object_creator(db,DailyMealPlan,date=newTimestamp,meal_id=meal_id).id
    recipeInMeal = simple_object_creator(db,RecipeInMeal,daily_meal_id = dailyMealId)
    recipe = get_by_id(db,Recipe,recipe_id).first()
    recipeInMeal.recipe.append(recipe)
    db.commit()
    return


def delete_week(db:Session,week_id:int):
    return delete(db, DailyMealPlan, week_id)
#
def get_week(db:Session,week_id:int):
    return get_by_id(db,DailyMealPlan,week_id).first()

def get_all_week(db:Session):
    return get_all_with_own_paginantion(db, DailyMealPlan)