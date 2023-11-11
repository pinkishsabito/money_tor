from uuid import UUID

from sqlalchemy import or_, select
from sqlalchemy.orm import sessionmaker

from main import engine
from src.transaction.entities import Transaction
from src.transaction.models import ModelTransaction

Session = sessionmaker(bind=engine)
session = Session()


async def get_all_related_data(bank_account_id: UUID):
    models = list(
        session.scalars(
            select(ModelTransaction)
            .where(
                or_(
                    ModelTransaction.from_id == bank_account_id,
                    ModelTransaction.to_id == bank_account_id
                )
            )
        )
    )
    return [
        [
            Transaction(
                id=model.id,
                created_at=model.created_at,
                amount=model.amount,
                from_id=model.from_id,
                to_id=model.to_id,
                currency_id=model.currency_id,
                category_id=model.category_id,
            )
            for model in models
            if model.from_id == bank_account_id
        ],
        [
            Transaction(
                id=model.id,
                created_at=model.created_at,
                amount=model.amount,
                from_id=model.from_id,
                to_id=model.to_id,
                currency_id=model.currency_id,
                category_id=model.category_id,
            )
            for model in models
            if model.to_id == bank_account_id
        ],
    ]

# session.add()
# session.commit()
# session.close()
