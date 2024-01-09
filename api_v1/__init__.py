from fastapi import APIRouter

from .cards.views import router as cards_router

router = APIRouter()
router.include_router(router=cards_router, prefix="/cards")
