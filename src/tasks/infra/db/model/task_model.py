import uuid

from sqlmodel import Field, SQLModel
from src.tasks.domain.task import Task


class TaskModel(SQLModel, table=True, schema="tasks"):
    id: uuid.UUID = Field(primary_key=True)
    name: str = Field()
    task_status: str = Field()
    description: str | None = Field(default=None)

    @staticmethod
    def from_task(task: Task):
        return TaskModel(
            id=task.id,
            name=task.name,
            task_status=task.task_status,
            description=task.description,
        )

    def to_task(self) -> Task:
        return Task(
            id=self.id,
            name=self.name,
            description=self.description,
            task_status=self.task_status,
        )
