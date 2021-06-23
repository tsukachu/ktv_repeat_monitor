from simple_settings import settings
from sqlalchemy_utils.functions import create_database, database_exists, drop_database

from app.database import get_url

settings.DATABASE["NAME"] = "test_" + settings.DATABASE["NAME"]
settings.configure(DATABASE=settings.DATABASE)


def setup():
    url = get_url(settings.DATABASE)
    if database_exists(url):
        drop_database(url)

    create_database(url)


def teardown():
    url = get_url(settings.DATABASE)
    if database_exists(url):
        drop_database(url)
