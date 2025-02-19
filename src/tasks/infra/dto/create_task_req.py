import uuid

from pydantic import BaseModel
from src.tasks.domain.task import Task, TaskStatus

class CreateTaskReq(BaseModel):
    name: str
    description: str
    task_status: TaskStatus

    def to_task(self) -> Task:
        return Task(
            id=uuid.uuid4(),
            name=self.name,
            description=self.description,
            task_status=self.task_status
        )