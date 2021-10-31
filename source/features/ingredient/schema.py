from typing import List

from pydantic import BaseModel

from source.features.product.schema import ProductBase


class Unit(BaseModel):
    name : str
    class Config:
        orm_mode = True


class IngredientBase(BaseModel):
    amount: int
    unit: List[Unit] = []
    product : List[ProductBase] = []
    class Config:
        orm_mode = True


class IngredientCreate(IngredientBase):
    recipe_id: int
    class Config:
        orm_mode = True


class Ingredient(IngredientBase):
    name: str
    product_id: int

    class Config:
        orm_mode = True
