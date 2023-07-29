from contextlib import asynccontextmanager
from typing import AsyncGenerator

from furl import furl
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.settings import settings


postgres_url = furl(settings.DATABASE_URL.unicode_string())
connect_args = {'timeout': 20}

# Digitalocean does not allow us to specify driver for the sting
if postgres_url.scheme == 'postgresql':
    postgres_url.scheme = 'postgresql+asyncpg'

# https://github.com/sqlalchemy/sqlalchemy/issues/6275
for key, value in postgres_url.query.params.items():
    connect_args[key] = value


async_engine = create_async_engine(
    postgres_url.url,
    future=True,
    connect_args=connect_args,
)
async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


@asynccontextmanager
async def async_session_scope() -> AsyncGenerator[AsyncSession, None]:
    session = async_session()
    try:
        yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()
