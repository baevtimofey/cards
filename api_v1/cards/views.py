from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import card_by_id
from .schemas import Card
from .schemas import CardCreate
from .schemas import CardUpdate

router = APIRouter(tags=["Cards"])


@router.get("/", response_model=list[Card])
async def get_cards(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_cards(session=session)


@router.post(
    "/",
    response_model=Card,
    status_code=status.HTTP_201_CREATED
)
async def create_card(
        card_in: CardCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_card(session=session, card_in=card_in)


@router.get("/{card_id}/", response_model=Card)
async def get_card(
        card: Card = Depends(card_by_id),
):
    return card


@router.put("/{card_id}/")
async def update_card(
        card_update: CardUpdate,
        card: Card = Depends(card_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_card(
        session=session,
        card=card,
        card_update=card_update,
    )
