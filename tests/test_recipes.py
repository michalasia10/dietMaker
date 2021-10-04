import json

import requests
from fastapi.testclient import TestClient

from db.get_db import get_db
from main import app
from tests.utils.overrides import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

JSON_PATH = 'tests/json_test/recipes.json'
RECIPE_JSON = json.load(open(JSON_PATH))

class TestGetRecipe:

    def test_get_all_recipes(self,requests_mock):
        requests_mock.get("http://127.0.0.1:8000/recipe",json=RECIPE_JSON)
        response = requests.get("http://127.0.0.1:8000/recipe")
        assert response.status_code == 200
        assert response.json() == RECIPE_JSON

