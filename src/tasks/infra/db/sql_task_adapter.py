import uuid

from sqlmodel import Session
from src.tasks.domain.task_port import TaskPort
from src.tasks.infra.db.model.task_model import TaskModel
from src.tasks.domain.task import Task


class SqlTaskAdapter(TaskPort):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: uuid.UUID) -> Task | None:
        task_db = self.session.get(TaskModel, id)
        if task_db is None:
            return None
        return task_db.to_task()

    def save(self, task: Task) -> Task:
        self.session.add(TaskModel.from_task(task))
        self.session.commit()
        return task

    def delete(self, id: uuid.UUID):
        task = self.session.get(TaskModel, id)
        self.session.delete(task)
        self.session.commit()