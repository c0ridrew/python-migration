from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configs import settings

conf = settings.databases.local
DATABASE = f"mysql://{conf.user_name}:{conf.password}@{conf.host}/{conf.database_name}"

engine = create_engine(DATABASE, encoding="utf-8", echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
