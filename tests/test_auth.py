from uuid import uuid4

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_me_without_token():
    response = client.get("/me")
    assert response.status_code == 401


def test_login_invalid_credentials():
    response = client.post(
        "/login",
        json={
            "email": "wrong@example.com",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401


def test_register_and_login():
    email = f"test_{uuid4().hex}@example.com"
    password = "TestPassword123"

    register_response = client.post(
        "/users",
        json={
            "name": "Test User",
            "email": email,
            "password": password
        }
    )

    assert register_response.status_code == 200

    login_response = client.post(
        "/login",
        json={
            "email": email,
            "password": password
        }
    )

    assert login_response.status_code == 200

    data = login_response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert "user_id" in data