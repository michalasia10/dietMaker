import json
from typing import Dict

from fastapi import HTTPException
from sqlalchemy.orm import Session


def warning(model, code, **kwargs):
    if 'id' in kwargs:
        raise HTTPException(
            status_code=code,
            detail=f"{model.__name__} with ID: {kwargs['id']} doesn't exist"

        )
    elif 'name' in kwargs:
        raise HTTPException(
            status_code=code,
            detail=f"{model.__name__} with name: {kwargs['name']} already exist"
        )


def get_all(db: Session, model):
    return db.query(model).offset(0).limit(100).all()


def get_by_id(db: Session, model, id: int):
    return db.query(model).filter(model.id == id)


def get_by_id_with_valid(db: Session, model, id: int):
    item = get_by_id(db, model, id)
    if not item.first():
        warning(model, 404, id=id)
    return item


def check_exist_by_name(db: Session, model, request: dict):
    name = request['name']
    return db.query(model).filter(model.name == name)


def create(db: Session, model, request):
    requestAsDict = json.loads(request.json())
    new_db_item = check_exist_by_name(db, model, requestAsDict)
    if new_db_item.first():
        warning(model, 400, name=requestAsDict['name'])
    new_db_item = model(**requestAsDict)
    db.add(new_db_item)
    db.commit()
    db.refresh(new_db_item)
    return new_db_item


def create_with_relation(db: Session, model, request):
    requestAsDict = json.loads(request.json())
    new_db_item = model(**requestAsDict)
    db.add(new_db_item)
    db.commit()
    db.refresh(new_db_item)
    return new_db_item


def delete(db: Session, model, id: int, ) -> Dict[str, str]:
    item = get_by_id_with_valid(db, model, id)
    item.delete(synchronize_session=False)
    db.commit()
    return {'detail': f'{model} ID: {id} deleted.'}


def update(db: Session, model, id: int, request: dict):
    item = get_by_id_with_valid(db, model, id)
    item.update(request)
    db.commit()
    return {'detail': f'{model} ID: {id} updated.'}
