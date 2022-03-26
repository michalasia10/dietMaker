from pydantic import BaseModel,validator
from typing import List,Optional
from datetime import datetime


from source.features.recipe.schema import RecipeInMeal



class Macro(BaseModel):
    protein: Optional[float] = 0
    fat: Optional[float] = 0
    carbo: Optional[float] = 0
    kcal: Optional[float] = 0

    @validator('protein', pre=True)
    def protein_validate(cls, dt):
        return round(dt,3)

    @validator('fat', pre=True)
    def fat_validate(cls, dt):
        return round(dt,3)

    @validator('carbo', pre=True)
    def carbo_validate(cls, dt):
        return round(dt,3)

    @validator('kcal', pre=True)
    def kcal_validate(cls, dt):
        return round(dt,3)


class UserWeek(BaseModel):
    id: int
    date:Optional[int] = 0
    recipes: List[RecipeInMeal] = []
    macro : Macro = {}

    @validator('date',pre=True)
    def date_validate(cls,dt):
        return dt.timestamp()

    class Config:
        orm_mode = True
        validate_assigment = True