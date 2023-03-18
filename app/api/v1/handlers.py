from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session

from app import schemas
from app.db import storage, db

tasks_router = APIRouter(prefix='/v1/tasks')


@tasks_router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=list[schemas.Task]
)
async def get_all_tasks(
        session: Session = Depends(db.get_session)
):
    tasks = storage.get_all_tasks(session)
    return tasks


@tasks_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.Task
)
async def create_task(
        task_schema: schemas.TaskCreate,
        session: Session = Depends(db.get_session)
):
    task = storage.create_task(session, task_schema)
    return task
