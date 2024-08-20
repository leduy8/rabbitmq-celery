from celery import shared_task
from fastapi import APIRouter

router = APIRouter(prefix="/celery", tags=["celery"])


@router.get("/")
async def test_celery():
    hello_world.delay()
    return "Your request will be handled by celery!"


@shared_task
def hello_world():
    return "Hello World from celery!"