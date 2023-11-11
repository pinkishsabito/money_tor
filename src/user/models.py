from sqlalchemy import TIMESTAMP, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, relationship, foreign

Base = declarative_base()


class LegalEntity(Base):
    __tablename__ = "legal_entities"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    first_name = mapped_column(VARCHAR(30), nullable=False)
    last_name = mapped_column(VARCHAR(30), nullable=False)
    dob = mapped_column(TIMESTAMP, nullable=False)


class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    name = mapped_column(VARCHAR(200), nullable=False)
    legal_entity_id = mapped_column(VARCHAR(36), nullable=False)

    owner_rel = relationship(LegalEntity, primaryjoin=foreign(legal_entity_id) == LegalEntity.id)
