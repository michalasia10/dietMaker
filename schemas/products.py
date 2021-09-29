from typing import Optional, List

from pydantic import BaseModel


class Tagsbase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


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
    tags: List[Tagsbase] = []

    class Config:
        orm_mode = True

