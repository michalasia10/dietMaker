from fastapi import FastAPI,Depends
import models,schemas,crud
from database import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def index():
    return 'hey'

@app.post('/create-category')
def create_category(request:schemas.CreateCategory,db:Session = Depends(get_db)):
    category = crud.create_category(db,request)
    return category

@app.get("/category/{category_id}",response_model=schemas.Category)
def get_category(category_id : int ,db:Session=Depends((get_db))):
    print(category_id)
    category = crud.get_category(db,category_id)
    return category