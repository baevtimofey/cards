from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class Card(Base):
    question: Mapped[str] = mapped_column(nullable=False)
    answer: Mapped[str] = mapped_column(nullable=False)
