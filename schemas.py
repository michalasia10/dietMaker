from typing import List, Optional
from pydantic import BaseModel

class CreateCategory(BaseModel):
    name : str
    pict_url : str

class Category(BaseModel):
    id:int
    name:str
    pict_url:str

    class Config:
        orm_mode = True