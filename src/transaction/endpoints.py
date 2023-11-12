from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.transaction.entities import Transaction
from src.transaction.models import ModelTransaction
from src.utils import DB_URL

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()


async def get_from_related_data(bank_account_id: str):
    models = list(
        session.query(ModelTransaction)
        .filter(ModelTransaction.from_id == str(bank_account_id))
        .all()
    )

    return [
        Transaction(
            id=model.id,
            created_at=model.created_at,
            amount=model.amount,
            from_id=model.from_id_rel.name,
            to_id=model.to_id_rel.name,
            currency_id=model.currency_rel.name,
            category_id=model.category_rel.name,
        )
        for model in models
        if model.from_id == str(bank_account_id)
    ]


async def get_to_related_data(bank_account_id: str):
    models = list(
        session.query(ModelTransaction)
        .filter(
            ModelTransaction.to_id == str(bank_account_id),
        )
        .all()
    )

    return [
        Transaction(
            id=model.id,
            created_at=model.created_at,
            amount=model.amount,
            from_id=model.from_id_rel.name,
            to_id=model.to_id_rel.name,
            currency_id=model.currency_rel.name,
            category_id=model.category_rel.name,
        )
        for model in models
        if model.to_id == str(bank_account_id)
    ]
