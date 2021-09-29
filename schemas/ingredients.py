from pydantic import BaseModel

from .products import ProductMakros


class IngredientBase(BaseModel):
    amount: int
    unit: str

    class Config:
        orm_mode = True


class IngredientCreate(IngredientBase):
    recipe_id: int
    product_id: int

    class Config:
        orm_mode = True


class Ingredient(IngredientBase):
    name: str
    product: ProductMakros

    class Config:
        orm_mode = True
