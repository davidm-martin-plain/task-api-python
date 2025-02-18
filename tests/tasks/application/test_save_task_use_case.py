import uuid

from unittest import mock, TestCase
from src.tasks.application.save_task_use_case import SaveTaskUseCase
from src.tasks.domain.task import Task, TaskStatus
from src.tasks.domain.task_port import TaskPort

port_mock = mock.MagicMock(TaskPort)


class SaveTaskUseCaseTest(TestCase):
    def test_save_task_use_case_returns_task(self):
        port_mock.save.return_value = TASK
        self.assertEqual(SaveTaskUseCase(task=TASK, port=port_mock).execute(), TASK)


TASK = Task(
    id=uuid.uuid4(),
    name="Test",
    description="Test description",
    task_status=TaskStatus.TODO,
)
