import unittest
import uuid

from unittest.mock import MagicMock
from src.shared.application.exception.not_found_exception import NotFoundException
from src.tasks.domain.task_port import TaskPort
from src.tasks.application.delete_task_use_case import DeleteTaskUseCase

port_mock = MagicMock(TaskPort)


class DeleteTaskUseCaseTest(unittest.TestCase):
    def test_delete_task_raises_not_found_exception(self):
        port_mock.get.return_value = None

        with self.assertRaisesRegex(NotFoundException, "Task not found"):
            DeleteTaskUseCase(uuid.uuid4(), port_mock).execute()

    def test_delete_not_existent_task_does_not_call_port_delete(self):
        port_mock.get.return_value = None
        try:
            DeleteTaskUseCase(uuid.uuid4(), port_mock).execute()
        except NotFoundException:
            port_mock.delete.assert_not_called()

    def test_delete_task_calls_port_delete(self):
        port_mock.get.return_value = MagicMock()

        DeleteTaskUseCase(uuid.uuid4(), port_mock).execute()

        port_mock.delete.assert_called_once()
