from fastapi import APIRouter

from app.types import StatsBlueprintSchema

router = APIRouter(
    prefix="/stats",
    tags=["status"],
)


@router.put("/")
async def put_stats(stats: StatsBlueprintSchema):
    return {}
