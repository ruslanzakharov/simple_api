from typing import Type

from sqlalchemy.orm import Session
import sqlalchemy.orm.exc as alc_exc

from app.db.models import Task
import app.schemas as schemas


def create_task(
        session: Session,
        task_schema: schemas.TaskCreateRequest
) -> Task:
    task = Task(description=task_schema.description, status=False)
    session.add(task)
    session.commit()
    session.refresh(task)

    return task


def get_all_tasks(session: Session) -> list[Type[Task]]:
    tasks = session.query(Task).all()
    return tasks


def get_task(session: Session, task_id: int) -> Task:
    task = session.query(Task).get(task_id)
    if task is None:
        raise alc_exc.NoResultFound

    return task


def delete_task(session: Session, task_id: int) -> None:
    task = get_task(session, task_id)
    session.delete(task)
    session.commit()


def update_task(
        session: Session,
        task_id: int,
        update_schema: schemas.TaskUpdateRequest
) -> Task:
    task = get_task(session, task_id)

    if update_schema.description is not None:
        task.description = update_schema.description
    if update_schema.status is not None:
        task.status = update_schema.status
    session.commit()

    return task
