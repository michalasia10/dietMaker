from pydantic import BaseModel
from typing import List
from source.features.user.week.schema import UserWeek

class UserMealBasic(BaseModel):
    id:int
    name: str
    class Config:
        orm_mode = True


class UserMeals(UserMealBasic):
    day_meals : List[UserWeek] = []

    class Config:
        orm_mode = True