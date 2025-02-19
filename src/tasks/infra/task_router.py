import uuid

from fastapi import APIRouter, Depends, HTTPException
from src.tasks.application.get_task_use_case import GetTaskUseCase
from src.tasks.application.save_task_use_case import SaveTaskUseCase
from src.tasks.infra.dto.create_task_req import CreateTaskReq
from src.tasks.infra.task_adapter import TaskAdapter
from src.tasks.infra.task_config import get_task_adapter
from src.tasks.infra.dto.task_res import TaskResponse
from src.tasks.application.delete_task_use_case import DeleteTaskUseCase

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/{id}", response_model=TaskResponse)
async def get_task(id: uuid.UUID, adapter: TaskAdapter = Depends(get_task_adapter)):
    task = GetTaskUseCase(id, adapter).execute()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskResponse.from_task(task)

@router.post("", response_model=TaskResponse)
async def save_task(create_task_req: CreateTaskReq, adapter: TaskAdapter = Depends(get_task_adapter)):
    return TaskResponse.from_task(SaveTaskUseCase(create_task_req.to_task(), adapter).execute())

@router.delete("/{id}")
async def delete_task(id: uuid.UUID, adapter: TaskAdapter = Depends(get_task_adapter)) -> None:
    DeleteTaskUseCase(id, adapter).execute()