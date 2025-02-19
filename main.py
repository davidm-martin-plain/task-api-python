from fastapi import FastAPI, HTTPException, Request
from src.shared.application.exception.not_found_exception import NotFoundException
from src.tasks.infra import task_router

app = FastAPI()

app.include_router(task_router.router)

@app.exception_handler(NotFoundException)
async def not_found_exception_handler(request: Request, exc: NotFoundException):
    raise HTTPException(status_code=404, detail=str(exc))

@app.get("/")
async def root():
    return {"message": "Hello World"}