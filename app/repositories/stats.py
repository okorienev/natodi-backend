from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ActionLog
from app.types import StatsBlueprintSchema


class StatsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, stats: StatsBlueprintSchema) -> None:
        for action in stats.actions:
            self.session.add(ActionLog(
                user_ident=stats.user_ident,
                question_id=action.question_id,
                action_name=action.action_name,
            ))

        await self.session.commit()
