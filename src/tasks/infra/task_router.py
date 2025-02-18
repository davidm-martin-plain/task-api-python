import uuid

from fastapi import APIRouter, Depends, HTTPException
from src.tasks.application.get_task_use_case import GetTaskUseCase
from src.tasks.application.save_task_use_case import SaveTaskUseCase
from src.tasks.domain.task import Task
from src.tasks.infra.dto.create_task_req import CreateTaskReq
from src.tasks.infra.task_adapter import TaskAdapter
from src.tasks.infra.task_config import get_task_adapter

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/{id}", response_model=Task)
async def get_task(id: uuid.UUID, adapter: TaskAdapter = Depends(get_task_adapter)):
    task = GetTaskUseCase(id, adapter).execute()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=Task)
async def save_task(createTaskReq: CreateTaskReq, adapter: TaskAdapter = Depends(get_task_adapter)):
    return SaveTaskUseCase(createTaskReq.to_task(), adapter).execute()