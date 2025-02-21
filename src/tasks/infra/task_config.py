from src.shared.infra.db_config import get_session
from src.tasks.infra.db.sql_task_adapter import SqlTaskAdapter

task_adapter = SqlTaskAdapter(next(get_session()))

def get_task_adapter() -> SqlTaskAdapter:
    return task_adapter

