from pydantic import BaseModel
from typing import List
from datetime import datetime
from source.features.recipe.schema import RecipeInMeal

class UserWeek(BaseModel):
    id: int
    date:datetime
    recipes: List[RecipeInMeal] = []

    class Config:
        orm_mode = True