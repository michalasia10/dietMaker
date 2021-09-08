from sqlalchemy.orm import Session
import models,schemas

def create_category(db:Session,request):
    db_category = models.Category(name=request.name,pict_url=request.pict_url)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db:Session,category_id):
    return db.query(models.Category).filter(models.Category.id == category_id).first()
