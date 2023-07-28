from app.repositories.stats import StatsRepository
from app.types import StatsBlueprintSchema


class SaveStatsInteractor:
    def __init__(self, stats_repository: StatsRepository):
        self.repository = stats_repository

    async def execute(self, stats: StatsBlueprintSchema) -> None:
        await self.repository.save(stats)
