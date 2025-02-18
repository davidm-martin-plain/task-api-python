from src.shared.application.use_case import UseCase
from src.tasks.domain.task import Task
from src.tasks.domain.task_port import TaskPort

class GetTaskUseCase(UseCase[Task]):
    def __init__(self, id: int, port: TaskPort):
        self.port = port
        self.id = id

    def execute(self) -> Task:
        return self.port.get(self.id)