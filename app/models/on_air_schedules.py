from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

from app.database import session

Base = declarative_base()


class OnAirSchedule(Base):
    __tablename__ = "on_air_schedules"

    query = session.query_property()

    id = Column(Integer, primary_key=True)
