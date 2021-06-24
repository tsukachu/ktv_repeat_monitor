from logging import getLogger

from simple_settings import settings
from sqlalchemy_utils.functions import create_database, database_exists, drop_database

from app.database import get_url

logger = getLogger(__name__)

settings.DATABASE["NAME"] = "test_" + settings.DATABASE["NAME"]
settings.configure(DATABASE=settings.DATABASE)


def setup():
    logger.info(f"Creating test database ('{settings.DATABASE['NAME']}') ...")
    url = get_url(settings.DATABASE)
    if database_exists(url):
        logger.info(f"Database '{settings.DATABASE['NAME']}' already exists")
        logger.info(f"Destroying old test database ('{settings.DATABASE['NAME']}') ...")
        drop_database(url)

    create_database(url)


def teardown():
    logger.info(f"Destroying test database ('{settings.DATABASE['NAME']}') ...")
    url = get_url(settings.DATABASE)
    if database_exists(url):
        drop_database(url)
