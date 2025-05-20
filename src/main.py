from fastapi import FastAPI
from sqlmodel import create_engine
from shared.infrastructure.api import router as shared_router

app = FastAPI()

app.include_router(shared_router)

# db_engine = create_engine()