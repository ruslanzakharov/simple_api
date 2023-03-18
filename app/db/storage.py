from typing import Type

from sqlalchemy.orm import Session
import sqlalchemy.orm.exc as alc_exc

from app.db.models import Task
import app.schemas as schemas


def create_task(session: Session, task_schema: schemas.TaskCreate) -> Task:
    task = Task(description=task_schema.description, status=False)
    session.add(task)
    session.commit()
    session.refresh(task)

    return task


def get_all_tasks(session: Session) -> list[Type[Task]]:
    tasks = session.query(Task).all()
    return tasks


def delete_task(session: Session, task_id: int) -> None:
    task = session.query(Task).get(task_id)
    if task is None:
        raise alc_exc.NoResultFound

    session.delete(task)
    session.commit()
