import uuid

from typing import List
from src.tasks.domain.task import Task
from src.tasks.domain.task_port import TaskPort


class TaskAdapter(TaskPort):
    tasks: List[Task] = []

    def get(self, id: uuid.UUID) -> Task:
        return next((task for task in self.tasks if task.id == id), None)

    def save(self, task: Task) -> Task:
        self.tasks.append(task)
        return task
