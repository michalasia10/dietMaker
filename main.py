from fastapi import FastAPI
from models import models
from db.database import engine
from routers import category


app = FastAPI(title='dietmaker')

models.Base.metadata.create_all(bind=engine)

app.include_router(category.router)



