from logging import getLogger

import requests

from app.scraping.pages import OnAirSchedulePage

logger = getLogger(__name__)


def run():
    session = requests.Session()
    page = OnAirSchedulePage(session)
    page.get()
    page.parse()
    while page.has_next:
        page.pop()
        logger.debug(page.get_title())
        schedules = page.get_schedules()
        for schedule in schedules:
            logger.debug(f"{schedule['on_air']}, {schedule['episode']}")
