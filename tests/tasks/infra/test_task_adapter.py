import copy
import uuid
import pytest

from sqlmodel import SQLModel, Session, create_engine
from src.tasks.infra.db.sql_task_adapter import SqlTaskAdapter
from src.tasks.domain.task import Task, TaskStatus
from tests.test_config import get_test_settings

engine = create_engine(get_test_settings().db_url)


@pytest.fixture(autouse=True, scope="module")
def setup_database():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


@pytest.fixture
def session():
    with Session(engine) as session:
        yield session


@pytest.fixture
def sql_task_adapter(session) -> SqlTaskAdapter:
    return SqlTaskAdapter(session)


def test_get_task_returns_task(sql_task_adapter: SqlTaskAdapter):
    new_task = create_task()
    task = sql_task_adapter.save(new_task)
    task = sql_task_adapter.get(new_task.id)
    assert task == new_task


def test_get_task_returns_none(sql_task_adapter: SqlTaskAdapter):
    task = sql_task_adapter.get(uuid.uuid4())
    assert task is None


def test_save_task_returns_task(sql_task_adapter: SqlTaskAdapter):
    new_task = create_task()
    task = sql_task_adapter.save(new_task)
    assert task == new_task


def test_delete_task_remove_task_from_database(sql_task_adapter: SqlTaskAdapter):
    new_task = create_task()
    task = sql_task_adapter.save(copy.replace(new_task, id=new_task.id))

    sql_task_adapter.delete(new_task.id)

    task = sql_task_adapter.get(new_task.id)
    assert task is None


def create_task():
    return Task(
        id=uuid.uuid4(), name="Test", description="Test", task_status=TaskStatus.TODO
    )
