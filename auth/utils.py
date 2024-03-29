from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from core.models import db_helper


async def get_user_db(
        session: AsyncSession = Depends(db_helper.get_async_session)
):
    yield SQLAlchemyUserDatabase(session, User)
