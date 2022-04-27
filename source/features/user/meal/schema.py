from typing import List, Optional

from pydantic import BaseModel, validator

from source.features.recipe.schema import RecipeInMeal
from source.features.user.week.schema import UserWeek


class UserMealBasic(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Meal(BaseModel):
    meal: str
    recipes: List[RecipeInMeal]


class UserMeals(BaseModel):
    date: Optional[int] = 0
    meals: List[Meal]

    class Config:
        orm_mode = True

    @validator('date', pre=True)
    def date_validate(cls, dt):
        return dt.timestamp()


class UserMealsWithoutQUery(UserMealBasic):
    day_meals: List[UserWeek] = []

    class Config:
        orm_mode = True
