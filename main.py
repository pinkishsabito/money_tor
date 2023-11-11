from fastapi import FastAPI
from sqlalchemy import create_engine
from src.user.models import Base as UserBase
from src.transaction.models import Base as TransactionBase
from src.utils import DB_URL

app = FastAPI()
engine = create_engine(DB_URL)
UserBase.metadata.create_all(engine)
TransactionBase.metadata.create_all(engine)


@app.get("/")
async def root():
    return {"message": "I am alive!"}
