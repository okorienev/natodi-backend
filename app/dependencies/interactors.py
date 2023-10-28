from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_async_session
from app.interactors.stats.save import SaveStatsInteractor
from app.repositories.stats import StatsRepository


async def get_save_stats_interactor(session: AsyncSession = Depends(get_async_session)):
    repository = StatsRepository(session)

    return SaveStatsInteractor(repository)
