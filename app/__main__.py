from fastapi import FastAPI

from app.api.v1 import routers
from app.db import Base, engine

Base.metadata.create_all(engine)


def bind_routers(application: FastAPI) -> None:
    for router in routers:
        application.include_router(router)


def get_application() -> FastAPI:
    application = FastAPI()
    bind_routers(application)

    return application


app = get_application()
