from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class CardBase(BaseModel):
    question: str
    answer: str


class CardCreate(CardBase):
    pass


class CardUpdate(CardCreate):
    pass


class CardUpdatePartial(CardCreate):
    question: Optional[str] = None
    answer: Optional[str] = None


class Card(CardBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
