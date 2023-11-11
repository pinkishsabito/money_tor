# main.py
import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine
from src.transaction.dashboard import init_dashboard
from src.transaction.models import Base
from src.utils import DB_URL

app = FastAPI()
engine = create_engine(DB_URL)
Base.metadata.create_all(engine)

# Initialize the dash app
dash_app = init_dashboard()

# Mount the dash app
app.mount("/dash", dash_app.server)

@app.get("/")
async def root():
    return {"message": "I am dead inside!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
