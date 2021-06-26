import os

import fire

from app.scraping.main import run
from app.utils.test import setup, teardown


class Manager:
    def __init__(self, settings=None):
        if not settings:
            settings = "app.settings.development"
        os.environ.setdefault("SIMPLE_SETTINGS", settings)

    def setup(self):
        setup()

    def teardown(self):
        teardown()

    def scraping(self):
        run()


if __name__ == "__main__":
    fire.Fire(Manager)
