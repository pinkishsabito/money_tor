from sqlalchemy import DATE, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import foreign, mapped_column, relationship

Base = declarative_base()


class ModelLegalEntity(Base):
    __tablename__ = "legal_entities"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    first_name = mapped_column(VARCHAR(30), nullable=False)
    last_name = mapped_column(VARCHAR(30), nullable=False)
    description = mapped_column(VARCHAR(250), nullable=False)
    dob = mapped_column(DATE, nullable=False)


class ModelBankAccount(Base):
    __tablename__ = "bank_accounts"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    name = mapped_column(VARCHAR(200), nullable=False)
    legal_entity_id = mapped_column(VARCHAR(36), nullable=False)

    owner_rel = relationship(
        ModelLegalEntity, primaryjoin=foreign(legal_entity_id) == ModelLegalEntity.id
    )
