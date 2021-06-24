SIMPLE_SETTINGS = {
    "CONFIGURE_LOGGING": True,
}

LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {
            "()": "app.logging.ColoredFormatter",
            "format": "{log_color}{levelname}{reset} {asctime} {module} {process:d} {thread:d} {message}",  # noqa
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console",
        ],
    },
    "disable_existing_loggers": False,
}

DATABASE = {
    "DIALECT": "postgresql",
    "DRIVER": "psycopg2",
    "USER": "",
    "PASSWORD": "",
    "HOST": "",
    "PORT": "",
    "NAME": "",
}
