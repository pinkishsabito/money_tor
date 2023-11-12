from sqlalchemy.orm import sessionmaker
from faker import Faker
from sqlalchemy import create_engine
from src.transaction.models import ModelCurrency, ModelCategory, ModelTransaction, Base
from src.user.models import ModelLegalEntity, ModelBankAccount
from uuid import uuid4
from random import randint, choice
import os
from sqlalchemy import func
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

with open('first_name.txt', 'r', encoding='utf-8') as file:
    first_names = [line.strip() for line in file.readlines()]

with open('last_name.txt', 'r', encoding='utf-8') as file:
    last_names = [line.strip() for line in file.readlines()]

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

categories_data = [
    {'id': 'aa0743f8-3790-4614-a855-e10c2da1dedf', 'name': 'Rent'},
    {'id': '570a586f-9663-4662-8c5c-268b1c61378e', 'name': 'Entertainment'},
    {'id': '40ae32ac-bb43-4580-9da1-e568a36b513f', 'name': 'Bills'},
    {'id': '7125a635-19c4-4958-95cd-42d2547cc087', 'name': 'SMM'},
    {'id': '055cb291-9456-4403-b0a7-db5f8d3b8a14', 'name': 'Salary'},
    {'id': '8d6e8129-2333-4aca-b61e-df4a71dea1c4', 'name': 'Others'}
]
# currency_data = [
#     {"id": 'dbc46a41-f1c5-40c7-92b1-c3a9e387bb08'}
# ]
session.bulk_insert_mappings(ModelCategory, categories_data)
session.commit()

legal_entities = []
for _ in range(200):
    first_name = choice(first_names)
    last_name = choice(last_names)
    legal_entity = ModelLegalEntity(
        id=str(uuid4()),
        first_name=first_name,
        last_name=last_name,
        dob=fake.date_of_birth()
    )
    legal_entities.append(legal_entity)

session.bulk_save_objects(legal_entities)
session.commit()

bank_accounts = []
for legal_entity in legal_entities:
    bank_account = ModelBankAccount(
        id=str(uuid4()),
        name=f"{legal_entity.first_name} {legal_entity.last_name}'s Account",
        legal_entity_id=legal_entity.id
    )
    bank_accounts.append(bank_account)
    session.add(bank_account)

session.commit()

transactions = []
for _ in range(30000):
    from_id = choice(bank_accounts)
    to_id = choice(bank_accounts)

    while from_id == to_id:
        to_id = choice(bank_accounts)

    amount = randint(800, 100000)
    created_at = fake.date_time_between(start_date='-1y', end_date='now')
    category = session.query(ModelCategory).order_by(func.rand()).first()

    transaction = ModelTransaction(
        id=str(uuid4()),
        from_id=from_id.id,
        to_id=to_id.id,
        amount=amount, currency_id='dbc46a41-f1c5-40c7-92b1-c3a9e387bb08',
        created_at=created_at,
        category_id=category.id
    )
    transactions.append(transaction)

session.bulk_save_objects(transactions)
session.commit()

session.close()
