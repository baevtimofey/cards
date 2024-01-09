from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1 import router as router_v1
from core.config import settings
from core.models import Base
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        conn: AsyncSession
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=8001)
