from typing import List

from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session


from crud.user_week import create_week,get_all_week,get_week,delete_week

from db.get_db import get_db
from schemas.user_weeks import UserWeek

router = APIRouter(
    prefix="/userweek",
    tags=["userweek"],
)

@router.get('/',
            response_model=List[UserWeek])
def get_all(db: Session = Depends(get_db)):
    return get_all_week(db)

@router.post('/create/{timestamp}/{meal_id}/{recipe_id}', status_code=status.HTTP_201_CREATED)
def create_new_week(timestamp:int,meal_id:int,recipe_id:int, db: Session = Depends(get_db)):
    return create_week(db,timestamp,meal_id,recipe_id)


@router.get('/{week_id}', response_model=UserWeek)
def get_week_by_id(week_id: int, db: Session = Depends(get_db)):
    return get_week(db, week_id)

@router.get('/delete/{week_id}', response_model=UserWeek)
def get_delete_by_id(week_id: int, db: Session = Depends(get_db)):
    return delete_week(db, week_id)


