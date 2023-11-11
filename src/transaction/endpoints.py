from sqlalchemy.orm import sessionmaker

from main import engine
from src.transaction.models import Base

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# session = Session()
# session.add()
# session.commit()
# session.close()
