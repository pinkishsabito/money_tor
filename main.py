from fastapi import FastAPI
from sqlalchemy import create_engine
from src.user.models import Base
from src.utils import DB_URL

app = FastAPI()
engine = create_engine(DB_URL)
Base.metadata.create_all(engine)


@app.get("/")
async def root():
    return {"message": "I am alive!"}
