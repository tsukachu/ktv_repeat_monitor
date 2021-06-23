from unittest import TestCase

from app.factories import OnAirScheduleFactory
from app.models import OnAirSchedule


class OnAirScheduleTests(TestCase):
    def test_create(self):
        on_air_schedule = OnAirScheduleFactory()
        self.assertTrue(
            OnAirSchedule.query.session.query(
                OnAirSchedule.query.filter(
                    OnAirSchedule.id == on_air_schedule.id
                ).exists()
            ).scalar()
        )
