from simple_settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(settings.DATABASE_URL)
session = scoped_session(sessionmaker(bind=engine))
