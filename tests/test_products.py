from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_cheapest_product():
    response = client.get("/products/cheapest")

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "name" in data
    assert "price" in data


def test_get_product_by_id():
    response = client.get("/products/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data
    assert "price" in data


def test_get_product_not_found():
    response = client.get("/products/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_create_product_without_token():
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "price": 100
        }
    )

    assert response.status_code == 401