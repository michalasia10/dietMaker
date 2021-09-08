from pydantic import BaseModel

class CategoryBase(BaseModel):
    name : str
    pict_url : str

class Category(CategoryBase):
    id:int

    class Config:
        orm_mode = True