from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session_scope


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_scope() as s:
        yield s
