from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    hashed_password: str

    class Config:
        orm_mode = True