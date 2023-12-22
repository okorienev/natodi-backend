from typing import Annotated

from fastapi import APIRouter, Depends, Query

from app.const import SEMVER_REGEX
from app.dependencies.auth import get_user_from_token_or_abort

router = APIRouter(
    prefix="/files",
    tags=["files"],
)


@router.get("/layout")
async def get_layout(app_version: str = Query(default=None, pattern=SEMVER_REGEX)):
    return {}


@router.get("/questions/{layout_id}")
async def get_questions(
    layout_id: str,
):
    return {}


@router.post("/authorization")
async def authorization(user: Annotated[dict, Depends(get_user_from_token_or_abort)]):
    return {"user": "user"}
