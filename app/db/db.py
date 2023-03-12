from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DB_URL = 'sqlite:///tasks.db'


engine = create_engine(
    SQLALCHEMY_DB_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def create_db():
    Base.metadata.create_all(bind=engine)
