from sqlalchemy.orm import Session
from models.category import Category

def create_category(db:Session,request):
    db_category = Category(name=request.name,pict_url=request.pict_url)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db:Session,category_id):
    return db.query(Category).filter(Category.id == category_id).first()
