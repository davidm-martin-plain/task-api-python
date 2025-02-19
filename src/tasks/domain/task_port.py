from abc import ABC, abstractmethod
import uuid
from src.tasks.domain.task import Task

class TaskPort(ABC):
    @abstractmethod
    def get(self, id: uuid.UUID) -> Task:
        pass

    @abstractmethod
    def save(self, task: Task) -> Task:
        pass

    @abstractmethod
    def delete(self, id: uuid.UUID) -> None:
        pass