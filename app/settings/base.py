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
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": [
                "console",
            ],
        },
    },
    "disable_existing_loggers": False,
}

# RFC 1738
# dialect(+driver)://username:password@host:port/database
DATABASE_URL = ""

TIME_ZONE = "Asia/Tokyo"
