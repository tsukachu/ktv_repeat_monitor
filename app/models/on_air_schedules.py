from sqlalchemy import Column, Integer, Text

from app.models import BaseModel, mixins
from app.models.types import DateTime


class OnAirSchedule(mixins.TimestampMixIn, BaseModel):
    __tablename__ = "on_air_schedules"

    title = Column(Text, nullable=False)
    episode = Column(Text, nullable=False)
    start = Column(DateTime(timezone=True), nullable=False)
    end = Column(DateTime(timezone=True), nullable=False)
    version = Column(Integer, default=1)


class OnAirScheduleSourceHistory(mixins.TimestampMixIn, BaseModel):
    __tablename__ = "on_air_schedule_source_history"

    source = Column(Text, nullable=False)
