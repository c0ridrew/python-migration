from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

user_name = "root"
password = "password"
host = "db"
database_name = "fastapi_practice_development"

DATABASE = f"mysql://{user_name}:{password}@{host}/{database_name}"

engine = create_engine(DATABASE, encoding="utf-8", echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
