from logging import getLogger

from simple_settings import settings
from sqlalchemy_utils.functions import create_database, database_exists, drop_database

from app.utils.database import add_prefix_to_database_name, get_database_name

logger = getLogger(__name__)


def setup():
    database_url = add_prefix_to_database_name(settings.DATABASE_URL)
    settings.configure(DATABASE_URL=database_url)

    database_name = get_database_name(settings.DATABASE_URL)
    logger.info(f"Creating test database ('{database_name}') ...")
    if database_exists(settings.DATABASE_URL):
        logger.info(f"Database '{database_name}' already exists")
        logger.info(f"Destroying old test database ('{database_name}') ...")
        drop_database(settings.DATABASE_URL)

    create_database(settings.DATABASE_URL)


def teardown():
    database_url = add_prefix_to_database_name(settings.DATABASE_URL)
    settings.configure(DATABASE_URL=database_url)

    database_name = get_database_name(settings.DATABASE_URL)
    logger.info(f"Destroying test database ('{database_name}') ...")
    if database_exists(settings.DATABASE_URL):
        drop_database(settings.DATABASE_URL)
