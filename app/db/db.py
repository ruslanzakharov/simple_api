from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DB_URL = 'sqlite:///tasks.db'


engine = create_engine(SQLALCHEMY_DB_URL)
Session = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(engine)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
