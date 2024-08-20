from fastapi import FastAPI

from app.celery import create_celery
from app.controllers import auth, celery, users
from app.database import Base, engine


def create_app() -> FastAPI:
    app = FastAPI()
    
    app.celery_app = create_celery()
    
    app.include_router(auth.router)
    app.include_router(users.router)
    app.include_router(celery.router)

    @app.get("/")
    async def index():
        return "Hello World"

    Base.metadata.create_all(engine)

    return app
