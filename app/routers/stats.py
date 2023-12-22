from fastapi import APIRouter, Depends
from starlette import status

from app.dependencies.interactors import get_save_stats_interactor
from app.interactors.stats.save import SaveStatsInteractor
from app.types import StatsBlueprintSchema

router = APIRouter(
    prefix="/stats",
    tags=["status"],
)


@router.put("/", status_code=status.HTTP_201_CREATED)
async def put_stats(
    stats: StatsBlueprintSchema,
    interactor: SaveStatsInteractor = Depends(get_save_stats_interactor),
):
    await interactor.execute(stats)

    return {"status": "ok"}
