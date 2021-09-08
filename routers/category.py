from fastapi import APIRouter, Depends,status
from db.get_db import get_db
from schemas.category import Category, CategoryBase
from crud.category import create_category, get_category, get_all_categories, delete_category
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/category",
    tags=["category"],

)


@router.get('/', response_model=List[Category])
def get_all(db: Session = Depends(get_db)):
    return get_all_categories(db)


@router.post('/create')
def create_new_category(request: CategoryBase, db: Session = Depends(get_db)):
    category = create_category(db, request)
    return category


@router.get("/{category_id}", response_model=Category)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db, category_id)
    return category


@router.delete("/delete/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(category_id: int, db: Session = Depends(get_db)):
    return delete_category(db, category_id)
