from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from source.core.app.database.get_db import get_db

from source.features.category.crud import create_category, get_category, get_all_categories, \
    delete_category, get_category_items, update_category
from source.features.category.schema import Category, CategoryBase, CategoryWithItems

version = APIRouter(
    prefix="/category",
    tags=["category"],
)


@version.get('/',
             response_model=List[Category])
def get_all(db: Session = Depends(get_db)):
    return get_all_categories(db)


@version.post('/create',
              status_code=status.HTTP_201_CREATED, )
def create_new_category(request: CategoryBase, db: Session = Depends(get_db)):
    category = create_category(db, request)
    return category


@version.get("/{category_id}",
             response_model=Category)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db, category_id)
    return category


@version.put("/{category_id}")
def update_category_by_id(request: CategoryBase, category_id: int, db: Session = Depends(get_db)):
    return update_category(db, category_id, request)


@version.delete("/delete/{category_id}",
                status_code=status.HTTP_204_NO_CONTENT)
def delete_category_by_id(category_id: int, db: Session = Depends(get_db)):
    return delete_category(db, category_id)



@version.get("/{category_id}/recipes",
             response_model=CategoryWithItems)
def get_category_with_recipes(category_id: int, db: Session = Depends(get_db)):
    return get_category_items(db, category_id)
