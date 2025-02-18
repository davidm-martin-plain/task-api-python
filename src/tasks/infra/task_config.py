from src.tasks.infra.task_adapter import TaskAdapter

task_adapter = TaskAdapter()

def get_task_adapter() -> TaskAdapter:
    return task_adapter