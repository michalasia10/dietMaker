from typing import List

from pydantic import BaseModel

from source.features.ingredient.schema import IngredientCreate


class RecipeBase(BaseModel):
    name: str
    pict_url: str
    category_id: int

    class Config:
        orm_mode = True


class RecipeInMeal(BaseModel):
    id : int
    recipe : List[RecipeBase] = []
    class Config:
        orm_mode = True


class RecipeWithIngredietns(RecipeBase):
    id: int
    ingredients: List[IngredientCreate] = []

    class Config:
        orm_mode = True