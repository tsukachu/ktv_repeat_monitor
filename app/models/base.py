from sqlalchemy.orm import declarative_base

from app.database import session
from app.models import mixins

Base = declarative_base()


class BaseModel(mixins.PrimaryKeyMixin, Base):
    __abstract__ = True

    query = session.query_property()
