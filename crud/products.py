from sqlalchemy.orm import Session

from models.models import Product
from .repeated_crud.repetead import get_by_id, create


def create_product(db:Session,request):
    return create(db,Product,request)

def get_product(db:Session,product_id):
    return get_by_id(db,Product,product_id).first()