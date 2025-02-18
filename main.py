from fastapi import FastAPI
from src.tasks.infra import task_router

app = FastAPI()

app.include_router(task_router.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}