from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    ENVIRONMENT: str
    DATABASE_URL: PostgresDsn

    SECRET_KEY: str
    ALGORITHM: str
    USERNAME: str
    ACCESS_TOKEN_EXPIRE_DAYS: int


settings = Settings(_env_file=".env")
