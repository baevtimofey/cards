from typing import Union

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Card
from .schemas import CardCreate
from .schemas import CardUpdate
from .schemas import CardUpdatePartial


async def get_cards(
        session: AsyncSession,
) -> list[Card]:
    stmt = select(Card).order_by(Card.id)
    result: Result = await session.execute(statement=stmt)
    cards = result.scalars().all()
    return cards


async def get_card(
        session: AsyncSession,
        card_id: int,
) -> Union[Card, None]:
    return await session.get(Card, card_id)


async def create_card(
        session: AsyncSession,
        card_in: CardCreate,
) -> Card:
    card = Card(**card_in.model_dump())
    session.add(card)
    await session.commit()
    await session.refresh(card)
    return card


async def update_card(
        session: AsyncSession,
        card: Card,
        card_update: Union[CardUpdate, CardUpdatePartial],
        partial: bool = False,
) -> Card:
    for field, value in card_update.model_dump(exclude_unset=partial).items():
        setattr(card, field, value)
    await session.commit()
    return card


async def delete_card(
        session: AsyncSession,
        card: Card,
) -> None:
    await session.delete(card)
    await session.commit()
