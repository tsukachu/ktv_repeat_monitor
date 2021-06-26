from runpy import run_module
from unittest import TestCase
from unittest.mock import patch

from main import Manager


class MainTests(TestCase):
    @patch("main.fire.Fire")
    def test_call_of_manager(self, mock_fire):
        run_module("main", run_name="__main__")

        mock_fire.assert_called()


class ManagerTests(TestCase):
    def setUp(self):
        self.manager = Manager()

    @patch("main.setup")
    def test_call_of_setup(self, mock_setup):
        self.manager.setup()

        mock_setup.assert_called()

    @patch("main.teardown")
    def test_call_of_teardown(self, mock_teardown):
        self.manager.teardown()

        mock_teardown.assert_called()

    @patch("main.run")
    def test_call_of_run(self, mock_run):
        self.manager.scraping()

        mock_run.assert_called()
