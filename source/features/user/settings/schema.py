from pydantic import BaseModel

class UserSettings(BaseModel):
    number_of_meals : int
    pro : bool = True