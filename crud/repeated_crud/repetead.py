from sqlalchemy.orm import Session

def get_all(db:Session,model):
    return db.query(model).offset(0).limit(100).all()

def get_by_id(db:Session,model,id):
    return db.query(model).filter(model.id == id)

def create(db:Session,model,request):
    requestAsDict = request.json()
    new_db_item = model(**requestAsDict)
    db.add(new_db_item)
    db.refresh(new_db_item)
    return db