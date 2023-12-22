import re

from pydantic import BaseModel

from app.const import SEMVER_REGEX


class SemVer(BaseModel):
    major: int
    minor: int
    fix: int

    @classmethod
    def from_str(cls, semver_str: str) -> "SemVer":
        parsed = re.match(SEMVER_REGEX, semver_str)
        if not parsed:
            raise ValueError("invalid semver string")

        return cls(
            major=parsed.group(1),
            minor=parsed.group(2),
            fix=parsed.group(3),
        )


class ActionBlueprintSchema(BaseModel):
    question_id: str
    action_name: str


class StatsBlueprintSchema(BaseModel):
    user_ident: str
    actions: list[ActionBlueprintSchema]
