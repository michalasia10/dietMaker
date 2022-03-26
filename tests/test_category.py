import json

import requests
from fastapi.testclient import TestClient

from source.core.app.database import get_db
from source.core.app.server import app
from tests.utils.overrides import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

JSON_PATH = 'tests/json_test/category.json'
PRODUCT_JSON = json.load(open(JSON_PATH))


BASIC_VALID_CATEGORY_JSON = PRODUCT_JSON["BASIC_VALID_CATEGORY_JSON"]

BASIC_INVALID_CATEGORY_JSON = PRODUCT_JSON["BASIC_INVALID_CATEGORY_JSON"]

CATEGORY_WITH_ITEMS = PRODUCT_JSON["CATEGORY_WITH_ITEMS"]

CATEGORY_ID = 1

class TestCreateCategory:

    def test_valid_create_category(self,test_db):
        response = client.post(
            'category/create',
            json=BASIC_VALID_CATEGORY_JSON
        )
        assert response.status_code == 201


    def test_invalid_create_category(self,test_db):
        response = client.post(
            'category/create',
            json=BASIC_INVALID_CATEGORY_JSON
        )
        assert response.status_code != 201

class TestGetCategory:

    def test_get_all_category(self,test_db):
        client.post(
            'category/create',
            json=BASIC_VALID_CATEGORY_JSON
        )
        response = client.get(
            'category/')
        assert response.status_code == 200
        assert isinstance(response.json(),list)


    def test_get_category_by_id_with_items(self,requests_mock):
        requests_mock.get(f"http://127.0.0.1:8000/category/{1}/recipes",
                          json=CATEGORY_WITH_ITEMS)
        response = requests.get(f"http://127.0.0.1:8000/category/{1}/recipes")
        assert response.status_code == 200
        assert response.json() == CATEGORY_WITH_ITEMS
        assert isinstance(response.json()['recipes'], list)




