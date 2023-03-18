from typing import Type

from sqlalchemy.orm import Session

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
    print(tasks[0])
    print(type([tasks[0]]))
    return tasks
