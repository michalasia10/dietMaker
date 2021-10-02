from sqlalchemy.orm import Session

from models.meal import Product
from .repeated_crud.repetead import get_by_id, create, get_all, delete


def create_product(db: Session, request):
    return create(db, Product, request)


def get_product(db: Session, product_id):
    return get_by_id(db, Product, product_id).first()


def get_all_product(skip:int,limit:int,db: Session):
    return get_all(db, Product,skip,limit)


def delete_product(db: Session, product_id):
    return delete(db, Product, product_id)
