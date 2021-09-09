from sqlalchemy.orm import Session
from models.models import Category
from .repeated_crud.repetead import get_by_id, create, get_all, delete


def create_category(db: Session, request):
    return create(db, Category, request)


def delete_category(db: Session, category_id):
    return delete(db, Category, category_id)


def get_category(db: Session, category_id):
    return get_by_id(db, Category, category_id).first()


def get_all_categories(db: Session):
    return get_all(db, Category)
