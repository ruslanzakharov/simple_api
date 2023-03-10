from fastapi import APIRouter

tasks_router = APIRouter(prefix='/v1/tasks')


@tasks_router.get('')
async def root():
    return {'message': 'My Tasks'}
