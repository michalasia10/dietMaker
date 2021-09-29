from pydantic import BaseModel

class UnitBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
