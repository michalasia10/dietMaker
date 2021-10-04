from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from crud.products import create_product, get_product, get_all_product, delete_product
from data.base_creator import product_creator
from db.get_db import get_db
from schemas.products import ProductBase, Product

router = APIRouter(
    prefix="/product",
    tags=["product"],
)


@router.get('/', response_model=List[Product])
def get_all(skip:int = 0, limit : int = 50,db: Session = Depends(get_db)):
    return get_all_product(skip,limit,db)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_new_product(request: ProductBase, db: Session = Depends(get_db)):
    return create_product(db, request)


@router.get('/{product_id}', response_model=Product)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    return get_product(db, product_id)


@router.delete('/delete/{product_id}')
def delete_products(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)


@router.post('/refresh-products-db/{password}')
def refresh_products_db(password:str,db: Session = Depends((get_db))):
    if password == 'michu':
        return product_creator(db)
