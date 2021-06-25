from unittest import TestCase

from app.utils.database import add_prefix_to_database_name, get_database_name


class DatabaseUtilsTests(TestCase):
    def setUp(self):
        self.database_url = "dialect+driver://username:password@host:port/database"

    def test_add_prefix_to_database_name(self):
        actual = add_prefix_to_database_name(self.database_url)
        expected = "dialect+driver://username:password@host:port/test_database"

        self.assertEqual(expected, actual)

    def test_get_database_name(self):
        actual = get_database_name(self.database_url)
        expected = "database"

        self.assertEqual(expected, actual)
