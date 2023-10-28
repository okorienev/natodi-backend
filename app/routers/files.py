from fastapi import APIRouter, Query

from app.const import SEMVER_REGEX

router = APIRouter(
    prefix="/files",
    tags=["files"],
)


@router.get("/layout")
async def get_layout(
    app_version: str = Query(default=None, pattern=SEMVER_REGEX)
):
    return {}


@router.get("/questions/{layout_id}")
async def get_questions(
    layout_id: str,
):
    return {}
