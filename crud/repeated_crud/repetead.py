from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import Dict


def get_all(db: Session, model):
    return db.query(model).offset(0).limit(100).all()


def get_by_id(db: Session, model, id: int):
    return db.query(model).filter(model.id == id)


def create(db: Session, model, request):
    requestAsDict = request.json()
    new_db_item = model(**requestAsDict)
    db.add(new_db_item)
    db.refresh(new_db_item)
    return db


def delete(db: Session, model, id: int, ) -> Dict[str, str]:
    item = get_by_id(db, model, id)
    if not item.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{model} with {id} doesn't exist"
        )
    item.delete(synchronize_session=False)
    db.commit()
    return {'detail': f'{model} ID: {id} deleted.'}
