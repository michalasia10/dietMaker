from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.app.core.database.database import Base
from src.app.core.database.database import engine
from routers import category, products, ingredients, \
    recipes, units,users,users_settings,user_meals,user_weeks,recipe_in_meal

app = FastAPI(title='dietmaker')

Base.metadata.create_all(bind=engine)

routers = [category,products,recipes,ingredients,
           units,users,users_settings,user_meals,user_weeks,recipe_in_meal]

for route in routers:
    app.include_router(route.router)

add_pagination(app)

