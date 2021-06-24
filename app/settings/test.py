from app.settings.base import *  # noqa

DATABASE.update(  # noqa
    {
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
        "NAME": "postgres",
    }
)
