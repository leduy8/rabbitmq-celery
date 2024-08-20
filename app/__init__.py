from fastapi import FastAPI

from app.controllers import auth, users
from app.database import Base, engine


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(auth.router)
    app.include_router(users.router)

    @app.get("/")
    async def index():
        return "Hello World"

    Base.metadata.create_all(engine)

    return app
