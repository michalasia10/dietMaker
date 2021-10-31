from sqlalchemy.orm import Session

from source.features.ingredient.models import Ingredient
from source.core.db_queries.crud import get_all_with_own_paginantion


def get_all_ingredietns(db: Session):
    return get_all_with_own_paginantion(db, Ingredient)


