import json

from fastapi.testclient import TestClient

from source.core.app.database import get_db
from source.core.app.server import app
from tests.utils.overrides import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

JSON_PATH = 'tests/json_test/products.json'
PRODUCT_JSON = json.load(open(JSON_PATH))


BASIC_VALID_PRODUCT_JSON = PRODUCT_JSON["BASIC_VALID_PRODUCT_JSON"]

BASIC_INVALID_PRODUCT_JSON = PRODUCT_JSON["BASIC_INVALID_PRODUCT_JSON"]



class TestCreateProduct:

    def test_valid_create_product(self,test_db):
        response = client.post(
            'product/create',
            json=BASIC_VALID_PRODUCT_JSON
        )
        assert response.status_code == 201


    def test_invalid_create_product(self,test_db):
        response = client.post(
            'product/create',
            json=BASIC_INVALID_PRODUCT_JSON
        )
        assert response.status_code != 201

    def test_create_same_product(self,test_db):
        responseFirst = client.post(
            'product/create',
            json=BASIC_VALID_PRODUCT_JSON
        )

        responseSecond = client.post(
            'product/create',
            json=BASIC_VALID_PRODUCT_JSON
        )
        assert  responseFirst.status_code == 201
        assert responseSecond.json() == {"detail": 'Product with name: Chicken already exist'}
        assert responseSecond.status_code == 400


class TestGetProduct:

    def test_get_products(self,test_db):
        client.post(
            'product/create',
            json=BASIC_VALID_PRODUCT_JSON
        )
        response = client.get(
            'product/'
        )
        assert response.status_code == 200
        assert response.json()[0]['code'] == BASIC_VALID_PRODUCT_JSON['code']
        assert isinstance(response.json(),list)


    def test_get_products_with_query(self,test_db):
        client.post(
            'product/create',
            json=BASIC_VALID_PRODUCT_JSON
        )
        response = client.get(
            'product/?skip=0&limit=1'
        )
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_get_product_by_id(self,test_db):
        client.post(
            'product/create',
            json=BASIC_VALID_PRODUCT_JSON
        )

        response = client.get(
            f'product/{1}'
        )
        assert response.status_code == 200
        assert response.json()['code'] == BASIC_VALID_PRODUCT_JSON['code']