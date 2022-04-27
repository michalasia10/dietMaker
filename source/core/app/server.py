import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from source.core.app.config import APP_NAME, SERVER_ADRESS, SERVER_PORT
from source.core.app.database.db import Base, engine
from source.core.app.routers import ROUTERS
import yaml
from os import path
def add_routers(app: FastAPI, routers: list):
    for route in routers:
        app.include_router(route)

def add_description()->list:
    path_file = path.abspath('docs/endpoints.yml')
    with open(path_file,'r') as file:
        return yaml.load(file,Loader=yaml.FullLoader)

def create_app() -> FastAPI:
    app = FastAPI(
        title=APP_NAME,
        # openapi_tags=add_description()
    )
    add_routers(app, ROUTERS)
    add_pagination(app)
    return app


app: FastAPI = create_app()
Base.metadata.create_all(bind=engine)


def run() -> None:
    uvicorn.run(app, host=SERVER_ADRESS, port=SERVER_PORT,workers=1)


