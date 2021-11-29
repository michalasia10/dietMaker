from pydantic import BaseModel,validator
from typing import List,Optional
from datetime import datetime
from source.features.recipe.schema import RecipeInMeal

class UserWeek(BaseModel):
    id: int
    date:Optional[int] = 0
    recipes: List[RecipeInMeal] = []

    @validator('date',pre=True)
    def date_validate(cls,dt):
        return dt.timestamp()

    class Config:
        orm_mode = True
        validate_assigment = True