from sqlalchemy.orm import sessionmaker
from faker import Faker
from sqlalchemy import create_engine
from src.transaction.models import Currency, Category, Transaction, Base
from src.user.models import User, LegalEntity
from uuid import uuid4
from random import randint, choice

# Создаем соединение с базой данных
engine = create_engine('ваша строка подключения к базе данных')
Session = sessionmaker(bind=engine)
session = Session()

# Создаем объект Faker для генерации случайных данных
fake = Faker()

# Читаем имена из файла
with open('first_name.txt', 'r', encoding='utf-8') as file:
    first_names = [line.strip() for line in file.readlines()]

# Читаем фамилии из файла
with open('last_name.txt', 'r', encoding='utf-8') as file:
    last_names = [line.strip() for line in file.readlines()]

with open('categories.txt', 'r', encding='utf-8') as file:
    categories = [line.strip() for line in file.readlines()]

# Очищаем таблицы перед заполнением
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Генерируем пользователей
users = []
for _ in range(100):
    first_name = choice(first_names)
    last_name = choice(last_names)
    user = User(id=str(uuid4()), first_name=first_name, last_name=last_name, dob=fake.date_of_birth())
    users.append(user)

session.bulk_save_objects(users)
session.commit()

# Генерируем юридические лица
legal_entities = []
for _ in range(50):
    legal_entity = LegalEntity(id=str(uuid4()), owner_id=users[_].id)
    legal_entities.append(legal_entity)

session.bulk_save_objects(legal_entities)
session.commit()

# Генерируем категории
categories = [Category(id=str(uuid4()), name=fake.word()) for _ in range(5)]
session.bulk_save_objects(categories)
session.commit()

# Генерируем транзакции
transactions = []
for _ in range(500):
    from_legal_entity = choice(legal_entities)
    to_legal_entity = choice(legal_entities)
    amount = randint(10000, 10000000)
    currency = 'KZT'
    created_at = fake.date_time_between(start_date='-4m', end_date='now')
    category = choice(categories)

    transaction = Transaction(id=str(uuid4()), from_id=from_legal_entity.id, to_id=to_legal_entity.id,
                              amount=amount, currency='KZT', created_at=created_at, category=category.id)
    transactions.append(transaction)

session.bulk_save_objects(transactions)
session.commit()

session.close()
