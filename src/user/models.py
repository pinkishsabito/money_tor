from sqlalchemy import TIMESTAMP, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    first_name = mapped_column(VARCHAR(30), nullable=False)
    last_name = mapped_column(VARCHAR(30), nullable=False)
    dob = mapped_column(TIMESTAMP, nullable=False)


class LegalEntity(Base):
    __tablename__ = "legal_entities"

    id = mapped_column(VARCHAR(36), primary_key=True, nullable=False)
    owner_id = mapped_column(VARCHAR(36), ForeignKey("users.id"), nullable=False)
