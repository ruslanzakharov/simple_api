from pydantic import BaseModel
from typing import Optional


class TaskCreateRequest(BaseModel):
    description: str


class TaskUpdateRequest(BaseModel):
    description: Optional[str] = None
    status: Optional[bool] = None


class TaskResponse(BaseModel):
    id: int
    description: str
    status: bool

    class Config:
        orm_mode = True
