from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.settings import settings
from app.utils.db import prepare_connect_args

postgres_dns, connect_args = prepare_connect_args(settings.DATABASE_URL.unicode_string())

async_engine = create_async_engine(
    postgres_dns,
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
