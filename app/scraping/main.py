from logging import getLogger

import requests

from app.database import session
from app.models import OnAirSchedule
from app.scraping.pages import OnAirSchedulePage

logger = getLogger(__name__)


def run():
    page = OnAirSchedulePage(requests.Session())
    page.get()
    page.parse()
    while page.has_next:
        page.pop()
        logger.debug(page.get_title())
        schedules = page.get_schedules()
        for schedule in schedules:
            logger.debug(
                f"{schedule['start']}, {schedule['end']}, {schedule['episode']}"
            )
            on_air = OnAirSchedule(
                title=page.get_title(),
                episode=schedule["episode"],
                start=schedule["start"],
                end=schedule["end"],
            )
            session.add(on_air)

    session.commit()
