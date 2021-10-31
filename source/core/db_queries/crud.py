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


def get_all_with_own_paginantion(db: Session, model,skip : int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()

def get_all_with_lib_paginantion(db: Session, model):
    return db.query(model).all()

def get_by_id(db: Session, model, id: int):
    return db.query(model).filter(model.id == id)


def get_by_code(db: Session, model, code: int):
    return db.query(model).filter(model.code == code)


def get_by_id_with_valid(db: Session, model, id: int):
    item = get_by_id(db, model, id)
    if not item.first():
        warning(model, 404, id=id)
    return item


def check_exist_by_name(db: Session, model, request: dict):
    name = request['name']
    return db.query(model).filter(model.name == name)


def simple_object_creator(db: Session, model, **krwags):
    model = model(**krwags)
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def create(db: Session, model, request):
    requestAsDict = json.loads(request.json())
    new_db_item = check_exist_by_name(db, model, requestAsDict)
    if new_db_item.first():
        warning(model, 400, name=requestAsDict['name'])
    return simple_object_creator(db, model, **requestAsDict)


def create_with_relation(db: Session, model, request):
    requestAsDict = json.loads(request.json())
    return simple_object_creator(db, model, **requestAsDict)


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
