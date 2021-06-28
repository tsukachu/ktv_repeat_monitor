import pytz
from simple_settings import settings
from sqlalchemy import DateTime
from sqlalchemy.types import TypeDecorator


class DateTime(TypeDecorator):
    impl = DateTime

    cache_ok = True

    def process_bind_param(self, value, diarect):
        return value

    def process_result_value(self, value, diarect):
        return value.astimezone(pytz.timezone(settings.TIME_ZONE))
