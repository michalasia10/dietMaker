from fastapi import FastAPI
from db.database import engine , Base
from routers import category


app = FastAPI(title='dietmaker')

Base.metadata.create_all(bind=engine)

app.include_router(category.router)



