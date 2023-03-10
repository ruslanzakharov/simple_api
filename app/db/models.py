from sqlalchemy import Column, Integer, String, DateTime

from .db import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    creation_date = Column(DateTime)
