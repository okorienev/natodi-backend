from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, field_validator
from furl import furl


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    ENVIRONMENT: str
    DATABASE_URL: PostgresDsn

    @field_validator("DATABASE_URL")
    @classmethod
    def process_url(cls, url: PostgresDsn):
        """Digitalocean does not allow us to customize driver in the url string and it default to psycopg2"""
        parts = furl(url.unicode_string())
        if parts.scheme == 'postgresql':
            parts.scheme = 'postgresql+asyncpg'

        new_url_string = parts.url
        return PostgresDsn(new_url_string)


settings = Settings(_env_file='.env')
