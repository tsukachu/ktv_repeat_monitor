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
