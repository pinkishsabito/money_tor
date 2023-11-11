from sqlalchemy import VARCHAR, TIMESTAMP, ForeignKey, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column

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
    from_id = mapped_column(VARCHAR(36), ForeignKey("legal_entities.id"), nullable=False)
    to_id = mapped_column(VARCHAR(36), ForeignKey("legal_entities.id"), nullable=False)
    amount = mapped_column(INTEGER, nullable=False)
    currency = mapped_column(VARCHAR(5), ForeignKey("currencies.name"), nullable=False)
    created_at = mapped_column(TIMESTAMP, nullable=False)
    category = mapped_column(VARCHAR(36), ForeignKey("category.id"), nullable=False)
