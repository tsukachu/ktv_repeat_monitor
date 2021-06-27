from sqlalchemy import Column, Integer, Text, func
from sqlalchemy.orm import declarative_base

from app.database import session
from app.models.types import DateTime

Base = declarative_base()


class OnAirSchedule(Base):
    __tablename__ = "on_air_schedules"

    query = session.query_property()

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    episode = Column(Text, nullable=False)
    start = Column(DateTime(timezone=True), nullable=False)
    end = Column(DateTime(timezone=True), nullable=False)
    version = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )
