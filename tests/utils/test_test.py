from unittest import TestCase
from unittest.mock import patch

from app.utils.test import setup, teardown


class TestUtilsTests(TestCase):
    @patch("app.utils.test.create_database")
    @patch("app.utils.test.database_exists", return_value=False)
    def test_create_database(self, mock_database_exists, mock_create_database):
        setup()
        mock_create_database.assert_called_once()

    @patch("app.utils.test.create_database")
    @patch("app.utils.test.drop_database")
    @patch("app.utils.test.database_exists", return_value=True)
    def test_drop_database_if_exists_is_true(
        self, mock_database_exists, mock_drop_database, mock_create_database
    ):
        setup()
        mock_drop_database.assert_called_once()
        mock_create_database.assert_called_once()

    @patch("app.utils.test.drop_database")
    @patch("app.utils.test.database_exists", return_value=True)
    def test_drop_database(self, mock_database_exists, mock_drop_database):
        teardown()
        mock_drop_database.assert_called_once()
