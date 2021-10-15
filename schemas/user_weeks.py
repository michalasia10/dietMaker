from pydantic import BaseModel
from typing import List
from .recipes import RecipeBase
from datetime import datetime
from .recipe_in_meal import RecipeInMeal

class UserWeek(BaseModel):
    id: int
    date:datetime
    recipes: List[RecipeInMeal] = []

    class Config:
        orm_mode = True