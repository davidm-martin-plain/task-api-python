import uuid

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_task_returns_not_found():
    response = client.get(f"/tasks/{uuid.uuid4()}")
    assert response.status_code == 404


def test_get_task_returns_ok():
    create_response = client.post("/tasks", json=TASK_JSON)
    response = client.get(f"/tasks/{create_response.json()['id']}")
    assert response.status_code == 200


def test_get_task_returns_task():
    create_response = client.post(
        "/tasks",
        json=TASK_JSON,
    )
    response = client.get(f"/tasks/{create_response.json()['id']}")
    assert response.json() == create_response.json()

def test_delete_task_returns_not_found():
    response = client.delete(f"/tasks/{uuid.uuid4()}")
    assert response.status_code == 404

def test_delete_task_returns_ok():
    create_response = client.post("/tasks", json=TASK_JSON)
    response = client.delete(f"/tasks/{create_response.json()['id']}")
    assert response.status_code == 200


TASK_JSON = {"name": "Test", "description": "Test description", "task_status": "todo"}
