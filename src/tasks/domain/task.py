from dataclasses import dataclass
from enum import Enum
import uuid

class TaskStatus(str, Enum):
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'

@dataclass
class Task:
    id: uuid.UUID
    name: str
    description: str
    task_status: TaskStatus
