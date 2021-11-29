from pydantic import BaseModel
from typing import List
from source.features.user.week.schema import UserWeek

class UserMealBasic(BaseModel):
    name: str

class UserMeals(UserMealBasic):
    day_meals : List[UserWeek] = []

    class Config:
        orm_mode = True