import uuid

from fastapi import Response

from main import app
from unittest.mock import patch
from fastapi.testclient import TestClient

from src.shared.application.exception.not_found_exception import NotFoundException
from src.tasks.domain.task import Task

client = TestClient(app)


def test_get_task_returns_not_found():
    with patch(GET_TASK, return_value=None):
        response = client.get(f"/tasks/{uuid.uuid4()}")
        assert response.status_code == 404


def test_get_task_returns_ok():
    with patch(GET_TASK, return_value=TASK):
        response = client.get(f"/tasks/{create_task().json()['id']}")
        assert response.status_code == 200


def test_get_task_returns_task():
    created_task = create_task()
    with patch(GET_TASK, return_value=TASK):
        print(created_task.json())
        response = client.get(f"/tasks/{created_task.json()['id']}")
        assert response.json() == created_task.json()


def test_delete_task_returns_not_found():
    with patch(DELETE_TASK, side_effect=NotFoundException("Task not found")):
        response = client.delete(f"/tasks/{uuid.uuid4()}")
        assert response.status_code == 404


def test_delete_task_returns_ok():
    with patch(DELETE_TASK, return_value=None):
        response = client.delete(f"/tasks/{create_task().json()['id']}")
        assert response.status_code == 200


def create_task() -> Response:
    with patch(CREATE_TASK, return_value=TASK):
        json_task = vars(TASK)
        json_task['id'] = str(json_task['id'])
        return client.post("/tasks", json=vars(TASK))


TASK: Task = Task(
    id=uuid.uuid4(), name="Test", description="Test description", task_status="todo"
)
GET_TASK = "src.tasks.application.get_task_use_case.GetTaskUseCase.execute"
DELETE_TASK = "src.tasks.application.delete_task_use_case.DeleteTaskUseCase.execute"
CREATE_TASK = "src.tasks.application.save_task_use_case.SaveTaskUseCase.execute"
