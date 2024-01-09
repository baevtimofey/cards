from typing import Annotated

from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Card
from core.models import db_helper
from . import crud


async def card_by_id(
        card_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Card:
    product = await crud.get_card(session=session, card_id=card_id)
    if product:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Card {card_id} not found!",
    )
