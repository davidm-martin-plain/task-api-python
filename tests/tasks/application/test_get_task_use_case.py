import uuid
from unittest import mock, TestCase
from src.tasks.application.get_task_use_case import GetTaskUseCase
from src.tasks.domain.task import Task, TaskStatus
from src.tasks.domain.task_port import TaskPort

task_port_mock = mock.Mock(spec=TaskPort)

class GetTaskUseCaseTest(TestCase):
    def test_get_task_use_case_returns_task(self):
        task_port_mock.get.return_value = TASK
        self.assertEqual(GetTaskUseCase(id=TASK.id, port=task_port_mock).execute(), TASK)


TASK = Task(
    id=uuid.uuid4(),
    name="Test",
    description="Test description",
    task_status=TaskStatus.TODO,
)