from typing import List

from pydantic import BaseModel

from .ingredients import IngredientCreate


class RecipeBase(BaseModel):
    name: str
    pict_url: str
    category_id: int

    class Config:
        orm_mode = True


class RecipeWithIngredietns(RecipeBase):
    id: int
    ingredients: List[IngredientCreate] = []
