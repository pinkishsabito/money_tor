from uuid import UUID

from fastapi import FastAPI

from src.transaction.endpoints import get_from_related_data, get_to_related_data

app = FastAPI()


@app.get("/")
async def root():
    pass


@app.get("/get_expense_related_data")
async def get_all_data(banking_account_id: UUID):
    return {
        "expense": await get_from_related_data(str(banking_account_id))
    }


@app.get("/get_income_related_data")
async def get_all_data(banking_account_id: UUID):
    return {
        "income": await get_to_related_data(str(banking_account_id))
    }
