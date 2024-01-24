from typing import Optional

from fastapi import Depends
from fastapi import Request
from fastapi_users import BaseUserManager
from fastapi_users import IntegerIDMixin

from .utils import get_user_db
from core.models import User
from core.config import settings


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = None
    verification_token_secret = settings.VERIFICATIONS_TOKEN_SECRET

    async def on_after_register(
            self, user: User,
            request: Optional[Request] = None
    ):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
            self, user: User,
            token: str,
            request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
            self, user: User,
            token: str,
            request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
