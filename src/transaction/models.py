from sqlalchemy import INTEGER, TIMESTAMP, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import foreign, mapped_column, relationship

from src.user.models import ModelBankAccount

Base = declarative_base()


class ModelCurrency(Base):
    __tablename__ = "currencies"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    name = mapped_column(VARCHAR(5), nullable=False)


class ModelCategory(Base):
    __tablename__ = "categories"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    name = mapped_column(VARCHAR(200), nullable=False)


class ModelTransaction(Base):
    __tablename__ = "transactions"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    created_at = mapped_column(TIMESTAMP, nullable=False)
    amount = mapped_column(INTEGER, nullable=False)
    from_id = mapped_column(VARCHAR(36), nullable=False)
    to_id = mapped_column(VARCHAR(36), nullable=False)
    currency_id = mapped_column(VARCHAR(36), nullable=False)
    category_id = mapped_column(VARCHAR(36), nullable=False)

    from_id_rel = relationship(
        ModelBankAccount, primaryjoin=foreign(from_id) == ModelBankAccount.id
    )
    to_id_rel = relationship(
        ModelBankAccount, primaryjoin=foreign(to_id) == ModelBankAccount.id
    )
    currency_rel = relationship(
        ModelCurrency, primaryjoin=foreign(currency_id) == ModelCurrency.id
    )
    category_rel = relationship(
        ModelCategory, primaryjoin=foreign(category_id) == ModelCategory.id
    )
