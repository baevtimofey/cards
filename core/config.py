from pathlib import Path

from pydantic import BaseModel
from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    db_echo: bool = True

    COOKIE_NAME: str
    COOKIE_MAX_AGE: int
    JWT_SECRET: str
    JWT_LIFETIME_SECONDS: int
    VERIFICATIONS_TOKEN_SECRET: str

    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env",
    )


settings = Settings()
