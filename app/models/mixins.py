from sqlalchemy import Column, Integer, func

from app.models.types import DateTime


class PrimaryKeyMixin:
    id = Column(Integer, primary_key=True)


class TimestampMixIn:
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )
