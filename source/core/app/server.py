import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination


from source.core.app.config import APP_NAME,SERVER_ADRESS,SERVER_PORT
from source.core.app.database.db import Base,engine
from source.core.app.routers import ROUTERS





def add_routers(app:FastAPI,routers:list):
    for route in routers:
        app.include_router(route)

def create_app()->FastAPI:
    app = FastAPI(
        title=APP_NAME
    )
    add_routers(app,ROUTERS)
    add_pagination(app)
    return app

app : FastAPI  = create_app()
Base.metadata.create_all(bind=engine)

def run()->None:
    uvicorn.run(app,host=SERVER_ADRESS,port=SERVER_PORT)


