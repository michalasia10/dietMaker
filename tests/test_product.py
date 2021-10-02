from fastapi.testclient import TestClient

from db.get_db import get_db
from main import app
from tests.utils.overrides import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)



BASIC_VALID_PRODUCT_JSON = {
            "code":2,
            "name":"Chicken",
            "pict_url":"www.google.com/chicken",
            "protein":25.0,
            "carbo":0.2,
            "fat":5,
            "kcal":200.0,
            'description':'',
        }

BASIC_INVALID_PRODUCT_JSON = {
            "code":'www.google.com/chicken',
            "name":2,
            "pict_url":22,
            "protein":"25.0",
            "carbo":"0.2",
            "fat":5,
            "kcal":"200.0",
        }


class TestCreateProduct:

    def test_valid_create_product(self,test_db):
        response = client.post(
            'product/create',
            json=BASIC_VALID_PRODUCT_JSON
        )
        assert response.status_code == 201
        assert response.json()['code'] == BASIC_VALID_PRODUCT_JSON['code']

    def test_invalid_create_product(self,test_db):
        response = client.post(
            'product/create',
            json=BASIC_INVALID_PRODUCT_JSON
        )
        assert response.status_code != 201

class TestGetProduct:

    def test_get_product(self,test_db):
        client.post(
            'product/create',
            json=BASIC_VALID_PRODUCT_JSON
        )
        response = client.get(
            'product/'
        )
        assert response.status_code == 200


    def test_get_product_with_query(self,test_db):
        client.post(
            'product/create',
            json=BASIC_VALID_PRODUCT_JSON
        )
        response = client.get(
            'product/?skip=0&limit=1'
        )
        assert response.status_code == 200
        assert len(response.json()) == 1
