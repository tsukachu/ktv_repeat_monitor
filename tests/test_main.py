from runpy import run_module
from unittest import TestCase
from unittest.mock import patch


class MainTests(TestCase):
    @patch("main.fire.Fire")
    def test_call_of_manager(self, mock_fire):
        run_module("main", run_name="__main__")

        mock_fire.assert_called()
