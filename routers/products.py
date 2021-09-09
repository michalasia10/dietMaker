from fastapi import APIRouter, Depends,status
from db.get_db import get_db
from schemas.products import ProductBase,Product
from crud.products import create_product, get_product
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

@router.post('/create',status_code=status.HTTP_201_CREATED)
def create_new_product(request:ProductBase,db: Session = Depends(get_db)):
    return create_product(db,request)

@router.get('/{product_id}',response_model=Product)
def get_product_by_id(product_id:int,db:Session = Depends(get_db)):
    return get_product(db,product_id)
