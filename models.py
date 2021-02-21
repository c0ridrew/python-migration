import enum

from sqlalchemy import Boolean, Column, Enum, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StatusEnum(str, enum.Enum):
    open = "open"
    clos = "clos"
    no = "no"


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    content = Column(String(300), nullable=False)
    account_status = Column(
        Enum(StatusEnum, values_callable=lambda obj: [e.value for e in obj])
    )
    donegg = Column(Boolean, default=False)
