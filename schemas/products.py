from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    pict_url: str
    protein: float
    carbo: float
    fat: float

    class Config:
        orm_mode = True


class ProductMakros(BaseModel):
    protein: float
    carbo: float
    fat: float

    class Config:
        orm_mode = True


class Product(ProductBase):
    id: int
    description: Optional[str] = None

    class Config:
        orm_mode = True

