from fastapi import APIRouter,Depends
from db.get_db import get_db
from schemas.category import Category,CategoryBase
from crud.category import create_category,get_category
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/category",
    tags=["category"],

)
get_db = get_db

@router.post('/create')
def create_new_category(request:CategoryBase,db:Session = Depends(get_db)):
    category = create_category(db,request)
    return category

@router.get("/{category_id}",response_model=Category)
def get_category_by_id(category_id : int ,db:Session=Depends((get_db))):
    category = get_category(db,category_id)
    return category