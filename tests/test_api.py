from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_empty_prompt():

    response = client.post(
        "/evaluate",
        json={"prompt": ""}
    )

    assert response.status_code == 400


def test_missing_prompt():

    response = client.post(
        "/evaluate",
        json={}
    )

    assert response.status_code == 422