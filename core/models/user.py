from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

from .base import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    username: Mapped[str] = mapped_column(String(30))
