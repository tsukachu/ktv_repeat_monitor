from datetime import datetime

import factory
import factory.fuzzy
import pytz

from app.database import session
from app.models import OnAirSchedule


class OnAirScheduleFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = OnAirSchedule
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "commit"

    title = factory.Sequence(lambda n: "Title %d" % n)
    episode = factory.Sequence(lambda n: "Episode %d" % n)
    start = factory.fuzzy.FuzzyDateTime(pytz.utc.localize(datetime(2021, 1, 1)))
    end = factory.fuzzy.FuzzyDateTime(pytz.utc.localize(datetime(2021, 1, 1)))
