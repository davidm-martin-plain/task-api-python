import uuid

from pydantic import BaseModel
from src.tasks.domain.task import Task, TaskStatus

class TaskResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str
    task_status: TaskStatus

    @staticmethod
    def from_task(task: Task) -> 'TaskResponse':
        return TaskResponse(
            id=task.id,
            name=task.name,
            description=task.description,
            task_status=task.task_status
        )

