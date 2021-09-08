from sqlalchemy.orm import Session
from models.models import Category
from fastapi import HTTPException,status

def get_by_id(db:Session,model,id):
    return db.query(model).filter(model.id == id)

def create_category(db:Session,request):
    db_category = Category(name=request.name,pict_url=request.pict_url)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db:Session,category_id):
    category = get_by_id(db,Category,category_id)
    if not category.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category_id} doesn't exist"
        )
    category.delete(synchronize_session=False)
    db.commit()
    return {'description':f'Category ID: {category_id} deleted.'}

def get_category(db:Session,category_id):
    category = get_by_id(db,Category,category_id).first()
    return category


def get_all_categories(db:Session):
    categories = db.query(Category).offset(0).limit(100).all()
    return categories