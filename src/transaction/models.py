from sqlalchemy import INTEGER, TIMESTAMP, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, relationship, foreign

from src.user.models import BankAccount

Base = declarative_base()


class Currency(Base):
    __tablename__ = "currencies"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    name = mapped_column(VARCHAR(5), nullable=False)


class Category(Base):
    __tablename__ = "categories"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    name = mapped_column(VARCHAR(200), nullable=False)


class Transaction(Base):
    __tablename__ = "transactions"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    created_at = mapped_column(TIMESTAMP, nullable=False)
    amount = mapped_column(INTEGER, nullable=False)
    from_id = mapped_column(VARCHAR(36), nullable=False)
    to_id = mapped_column(VARCHAR(36), nullable=False)
    currency_id = mapped_column(VARCHAR(36), nullable=False)
    category_id = mapped_column(VARCHAR(36), nullable=False)

    from_id_rel = relationship(BankAccount, primaryjoin=foreign(from_id) == BankAccount.id)
    to_id_rel = relationship(BankAccount, primaryjoin=foreign(to_id) == BankAccount.id)
    currency_rel = relationship(Currency, primaryjoin=foreign(currency_id) == Currency.id)
    category_rel = relationship(Category, primaryjoin=foreign(category_id) == Category.id)
