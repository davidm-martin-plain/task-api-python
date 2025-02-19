import uuid
from src.shared.application.exception.not_found_exception import NotFoundException
from src.shared.application.use_case import UseCase
from src.tasks.domain.task_port import TaskPort


class DeleteTaskUseCase(UseCase[None]):
    def __init__(self, id: uuid.UUID, port: TaskPort):
        self.id = id
        self.port = port

    def execute(self) -> None:
        if self.port.get(self.id) is None:
            raise NotFoundException("Task not found")
        self.port.delete(self.id)