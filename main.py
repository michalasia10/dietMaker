from fastapi import FastAPI

from db.database import Base
from db.database import engine
from routers import category, products, ingredients, recipes, units

app = FastAPI(title='dietmaker')

Base.metadata.create_all(bind=engine)

app.include_router(category.router)
app.include_router(products.router)
app.include_router(recipes.router)
app.include_router(ingredients.router)
app.include_router(units.router)
