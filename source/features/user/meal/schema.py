from pydantic import BaseModel, validator
from typing import List, Optional
from source.features.user.week.schema import UserWeek





class UserMealBasic(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class UserMeals(UserMealBasic):
    day_meals: List[UserWeek] = []

    class Config:
        orm_mode = True

    @validator('day_meals', pre=True)
    def day_meals__validate(cls, dt):
        return dt.all()


class UserMealsWithoutQUery(UserMealBasic):
    day_meals: List[UserWeek] = []

    class Config:
        orm_mode = True
