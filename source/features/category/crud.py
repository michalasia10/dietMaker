from sqlalchemy.orm import Session

from .models import Category
from source.core.db_queries.crud import get_by_id_with_valid, create, get_all_with_own_paginantion, delete, update


def create_category(db: Session, request):
    return create(db, Category, request)


def delete_category(db: Session, category_id: int):
    return delete(db, Category, category_id)


def get_category(db: Session, category_id: int):
    return get_by_id_with_valid(db, Category, category_id).first()


def get_all_categories(db: Session):
    return get_all_with_own_paginantion(db, Category)


def get_category_items(db: Session, category_id: int):
    return get_by_id_with_valid(db, Category, category_id).first()


def update_category(db: Session, category_id: int, request):
    return update(db, Category, category_id, request)
