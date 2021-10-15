from tests.utils.settings_db import TestingSession


def override_get_db():
    try:
        db = TestingSession()
        yield db
    finally:
        db.close()

