from simple_settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def get_url(settings_database):
    return "{DIALECT}+{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}".format(
        **settings_database
    )


url = get_url(settings.DATABASE)

engine = create_engine(url)
session = scoped_session(sessionmaker(bind=engine))
