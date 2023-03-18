from pydantic import BaseModel


class TaskBase(BaseModel):
    description: str


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    description: str
    status: bool

    class Config:
        orm_mode = True
