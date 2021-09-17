from sqlalchemy.orm import Session

from models.models import Category
from .repeated_crud.repetead import get_by_id_with_valid, create, get_all, delete, update


def create_category(db: Session, request):
    return create(db, Category, request)


def delete_category(db: Session, category_id: int):
    return delete(db, Category, category_id)


def get_category(db: Session, category_id: int):
    return get_by_id_with_valid(db, Category, category_id).first()


def get_all_categories(db: Session):
    return get_all(db, Category)


def get_category_items(db: Session, category_id: int):
    return get_by_id_with_valid(db, Category, category_id).first()


def update_category(db: Session, category_id: int, request):
    return update(db, Category, category_id, request)
