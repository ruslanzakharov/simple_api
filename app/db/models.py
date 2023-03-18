from sqlalchemy import Column, Integer, String, Boolean

from .db import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    status = Column(Boolean)
