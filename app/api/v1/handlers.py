from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
import sqlalchemy.orm.exc as alc_exc

from app import schemas
from app.db import storage, db

tasks_router = APIRouter(prefix='/v1/tasks')


@tasks_router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=list[schemas.TaskResponse]
)
async def get_all_tasks(
        session: Session = Depends(db.get_session)
):
    tasks = storage.get_all_tasks(session)
    return tasks


@tasks_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.TaskResponse
)
async def create_task(
        task_schema: schemas.TaskCreateRequest,
        session: Session = Depends(db.get_session)
):
    task = storage.create_task(session, task_schema)
    return task


@tasks_router.delete(
    '/{task_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_task(
        task_id: int,
        session: Session = Depends(db.get_session)
):
    try:
        storage.delete_task(session, task_id)
    except alc_exc.NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task not found'
        )


@tasks_router.put(
    '/{task_id}',
    status_code=status.HTTP_200_OK,
    response_model=schemas.TaskResponse
)
async def update_task(
        task_id: int,
        update_schema: schemas.TaskUpdateRequest,
        session: Session = Depends(db.get_session)
):
    try:
        task = storage.update_task(session, task_id, update_schema)
    except alc_exc.NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task not found'
        )
    return task


@tasks_router.get(
    '/{task_id}',
    status_code=status.HTTP_200_OK,
    response_model=schemas.TaskResponse
)
async def get_task(
        task_id: int,
        session: Session = Depends(db.get_session)
):
    try:
        task = storage.get_task(session, task_id)
        return task
    except alc_exc.NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task not found'
        )
