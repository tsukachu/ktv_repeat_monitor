import factory

from app.database import session
from app.models import OnAirSchedule


class OnAirScheduleFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = OnAirSchedule
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: n)
