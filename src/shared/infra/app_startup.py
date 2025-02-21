from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.shared.infra.db_config import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield