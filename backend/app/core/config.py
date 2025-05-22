from functools import lru_cache
from pathlib import Path
from pydantic import BaseSettings, Field

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    env: str = Field("dev", env="ENVIRONMENT")
    db_url: str = Field(f"sqlite:///{BASE_DIR.parent / 'data' / 'poop.db'}", env="POOP_DB")
    api_prefix: str = "/api/v1"

    class Config:
        env_file = BASE_DIR.parent.parent / ".env"
        case_sensitive = True

@lru_cache
def get_settings() -> Settings:
    return Settings()  # cached singleton
