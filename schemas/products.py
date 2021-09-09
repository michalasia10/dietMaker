from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name : str
    category_id : int
    pict_url : str
    protein : float
    carbo :float
    fat : float

    class Config:
        orm_mode = True


class Product(ProductBase):
    id: int
    description : Optional[str] = None

    class Config:
        orm_mode = True

