from typing import List

from pydantic import BaseModel

from .recipes import RecipeWithIngredietns


class CategoryBase(BaseModel):
    name: str
    pict_url: str

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
