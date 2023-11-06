from datetime import datetime

from sqlalchemy import DateTime, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class ActionLog(Base):
    __tablename__ = "action_log"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    user_ident: Mapped[str] = mapped_column(String(256))
    question_id: Mapped[str] = mapped_column(String(256))
    action_name: Mapped[str] = mapped_column(String(256))

    __table_args__ = (
        Index("ix_action_log_created_at", created_at),
        Index("ix_action_log_action_name", action_name),
    )
