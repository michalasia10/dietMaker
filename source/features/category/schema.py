from typing import List

from pydantic import BaseModel, HttpUrl

from source.features.recipe.schema import RecipeWithIngredietns


class CategoryBase(BaseModel):
    name: str
    pict_url: HttpUrl

    class Config:
        orm_mode = True


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class CategoryWithItems(Category):
    recipes: List[RecipeWithIngredietns] = []

    class Config:
        orm_mode = True
