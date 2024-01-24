from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1 import router as router_v1
from auth import router as router_auth_jwt
from core.config import settings
from auth.helper import auth_backend
from auth.schemas import UserRead
from auth.schemas import UserCreate


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(
    router_auth_jwt.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    router_auth_jwt.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=8001)
