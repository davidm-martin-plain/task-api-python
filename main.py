from fastapi import FastAPI, HTTPException, Request
from src.shared.infra.app_startup import lifespan
from src.shared.application.exception.not_found_exception import NotFoundException
from src.tasks.infra.rest import task_router

app = FastAPI(lifespan=lifespan)

@app.exception_handler(NotFoundException)
async def not_found_exception_handler(request: Request, exc: NotFoundException):
    raise HTTPException(status_code=404, detail=str(exc))

app.include_router(task_router.router)