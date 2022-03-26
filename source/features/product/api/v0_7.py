from fastapi import APIRouter, Depends, status
from fastapi_pagination import LimitOffsetPage,paginate
from sqlalchemy.orm import Session
from typing import List
from source.core.app.database.get_db import get_db
from source.features.product.schema import ProductBase, Product
from source.features.product.crud import search_product
from source.features.product.api.v0_3 import version

version_0_7 = APIRouter(
    prefix="",
    tags=["product"],
)

version_0_7.include_router(version)

@version_0_7.get('/search',response_model=List[Product])
def search(query_string:str,db: Session = Depends(get_db)):
    return search_product(db,query_string)