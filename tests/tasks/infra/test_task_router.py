import uuid

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_task_returns_not_found():
    response = client.get(f"/tasks/{uuid.uuid4()}")
    assert response.status_code == 404


def test_get_task_returns_ok():
    response = client.get(f"/tasks/{create_task().json()['id']}")
    assert response.status_code == 200


def test_get_task_returns_task():
    created_task = create_task()
    response = client.get(f"/tasks/{created_task.json()['id']}")
    assert response.json() == created_task.json()

def test_delete_task_returns_not_found():
    response = client.delete(f"/tasks/{uuid.uuid4()}")
    assert response.status_code == 404

def test_delete_task_returns_ok():
    response = client.delete(f"/tasks/{create_task().json()['id']}")
    assert response.status_code == 200

def create_task():
    return client.post("/tasks", json=TASK_JSON)


TASK_JSON = {"name": "Test", "description": "Test description", "task_status": "todo"}
