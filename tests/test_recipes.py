import json

import requests
from fastapi.testclient import TestClient

from source.core.app.database import get_db
from source.core.app.server import app
from tests.utils.overrides import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

JSON_PATH = 'tests/json_test/recipes.json'
RECIPE_JSON = json.load(open(JSON_PATH))

RECIPE_ID = 3

class TestGetRecipe:

    def test_get_all_recipes(self,requests_mock):
        requests_mock.get("http://127.0.0.1:8000/recipe",
                          json=RECIPE_JSON)
        response = requests.get("http://127.0.0.1:8000/recipe")
        assert response.status_code == 200
        assert response.json() == RECIPE_JSON
        assert isinstance(response.json(),list)

    def test_get_recipe_by_id(self,requests_mock):
        requests_mock.get(f"http://127.0.0.1:8000/recipe/{RECIPE_ID}",json=RECIPE_JSON[0])
        response = requests.get(f"http://127.0.0.1:8000/recipe/{RECIPE_ID}")
        assert response.status_code == 200
        assert response.json() == RECIPE_JSON[0]

