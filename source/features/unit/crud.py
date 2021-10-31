from sqlalchemy.orm import Session

from source.features.unit.models import Unit
from source.core.db_queries.crud  import create, get_all_with_own_paginantion, get_by_id_with_valid, delete


def get_all_units(db: Session):
    return get_all_with_own_paginantion(db, Unit)


def get_unit_by_id(db: Session, unit_id: int):
    return get_by_id_with_valid(db, Unit, unit_id).first()


def create_unit(db: Session, request):
    return create(db, Unit, request)


def delete_unit(db: Session, recipe_id: int):
    return delete(db, Unit, recipe_id)

