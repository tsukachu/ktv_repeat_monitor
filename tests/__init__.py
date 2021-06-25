from simple_settings import settings

from app.utils.database import add_prefix_to_database_name

database_url = add_prefix_to_database_name(settings.DATABASE_URL)
settings.configure(DATABASE_URL=database_url)
