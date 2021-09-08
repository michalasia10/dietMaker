from sqlalchemy.orm import Session

def get_by_id(db:Session,model,id):
    return db.query(model).filter(model.id == id)