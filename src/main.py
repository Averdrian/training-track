import os
from dotenv import load_dotenv
from fastapi import FastAPI
from sqlmodel import create_engine
from shared.infrastructure.api import router as shared_router


load_dotenv()

app = FastAPI()

app.include_router(shared_router)


psql_engine = create_engine(f"postgresql://{os.getenv('user')}:{os.getenv('password')}@{os.getenv('host')}:{os.getenv('port')}/{os.getenv('db_name')}")
