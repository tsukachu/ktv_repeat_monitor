import os

import fire


class Manager:
    def __init__(self, settings=None):
        if not settings:
            settings = "app.settings.development"
        os.environ.setdefault("SIMPLE_SETTINGS", settings)


if __name__ == "__main__":
    fire.Fire(Manager)
