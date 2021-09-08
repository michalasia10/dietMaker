from fastapi import FastAPI
from db.database import Base
from routers import category
from db.database import engine
from models import models


app = FastAPI(title='dietmaker')

models.Base.metadata.create_all(bind=engine)


app.include_router(category.router)



