from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    ENVIRONMENT: str
    DATABASE_URL: PostgresDsn


settings = Settings(_env_file='.env')
