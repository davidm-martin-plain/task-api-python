from sqlmodel import SQLModel, Session, create_engine
from src.shared.infra.config_settings import get_settings

engine = create_engine(get_settings().db_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
