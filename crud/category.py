from sqlalchemy.orm import Session
from models.models import Category
from fastapi import HTTPException, status
from .repeated_crud.repetead import get_by_id, create, get_all


def create_category(db: Session, request):
    return create(db, Category, request)


def delete_category(db: Session, category_id):
    category = get_by_id(db, Category, category_id)
    if not category.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category_id} doesn't exist"
        )
    category.delete(synchronize_session=False)
    db.commit()
    return {'description': f'Category ID: {category_id} deleted.'}


def get_category(db: Session, category_id):
    return get_by_id(db, Category, category_id).first()


def get_all_categories(db: Session):
    return get_all(db, Category)
