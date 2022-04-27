import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, status
from fastapi_pagination import LimitOffsetPage, paginate
from sqlalchemy.orm import Session

from source.core.app.database.get_db import get_db
from source.core.data.base_creator import product_creator
from source.docs.doc import doc, create_docs
from source.features.product.crud import create_product, get_product, get_all_product, delete_product
from source.features.product.schema import ProductBase, Product

load_dotenv()
PASSWORD = os.environ.get('REFRESH_PASSWORD')

TAG = 'product'

version = APIRouter(
    prefix="/product",
    tags=[TAG],
)


@version.get('/', response_model=LimitOffsetPage[Product])
@doc(create_docs(TAG,'get_all'))
def get_all(db: Session = Depends(get_db)):
    return paginate(get_all_product(db))


@version.post('/create', status_code=status.HTTP_201_CREATED)
def create_new_product(request: ProductBase, db: Session = Depends(get_db)):
    return create_product(db, request)


@version.get('/{product_id}', response_model=Product)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    return get_product(db, product_id)


@version.delete('/delete/{product_id}')
def delete_products(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)


@version.post('/refresh-products-db/{password}')
def refresh_products_db(password: str, db: Session = Depends((get_db))):
    if password == PASSWORD:
        return product_creator(db)
