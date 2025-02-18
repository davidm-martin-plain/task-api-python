from src.shared.application.use_case import UseCase
from src.tasks.domain.task import Task

class SaveTaskUseCase(UseCase[Task]):
    def __init__(self, task, port):
        self.task = task
        self.port = port

    def execute(self) -> Task:
        return self.port.save(self.task)