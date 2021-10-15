from typing import List

from pydantic import BaseModel
from .recipes import RecipeBase

class RecipeInMeal(BaseModel):
    id : int
    recipe : List[RecipeBase] = []
    class Config:
        orm_mode = True