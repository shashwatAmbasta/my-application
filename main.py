from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.db.session import Base
from app.db.database import engine
from app.models import Employee  # registers the model with Base.metadata
from app.routes import app_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="My First Api", lifespan=lifespan)
app.include_router(app_router)