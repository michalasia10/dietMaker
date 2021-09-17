from fastapi import FastAPI

from db.database import engine
from models import models
from routers import category, products, ingredients, recipes

app = FastAPI(title='dietmaker')

models.Base.metadata.create_all(bind=engine)

app.include_router(category.router)
app.include_router(products.router)
app.include_router(recipes.router)
app.include_router(ingredients.router)
