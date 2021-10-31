from sqlalchemy.orm import Session

from source.features.product.models import Product
from source.core.db_queries.crud  import get_by_id, create, get_all_with_lib_paginantion, delete


def create_product(db: Session, request):
    return create(db, Product, request)


def get_product(db: Session, product_id):
    return get_by_id(db, Product, product_id).first()


def get_all_product(db: Session):
    return get_all_with_lib_paginantion(db, Product)

def delete_product(db: Session, product_id):
    return delete(db, Product, product_id)
