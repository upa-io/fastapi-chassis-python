import unittest
from datetime import datetime
from app.utils import Utils

class TestUtils(unittest.TestCase):

    def test_generate_current_datetime(self):
        result = Utils.generate_current_datetime()
        self.assertIsInstance(result, str)
        self.assertTrue(datetime.fromisoformat(result))

    def test_days_between_dates(self):
        date1 = datetime(2020, 1, 1)
        date2 = datetime(2020, 1, 11)
        result = Utils.days_between_dates(date1, date2)
        self.assertEqual(result, 10)

    def test_string_to_datetime(self):
        date_string = "2020-01-01"
        result = Utils.string_to_datetime(date_string)
        expected = datetime(2020, 1, 1)
        self.assertEqual(result, expected)

    def test_get_first_day_of_month(self):
        date = datetime(2020, 1, 15)
        result = Utils.get_first_day_of_month(date)
        expected = datetime(2020, 1, 1)
        self.assertEqual(result, expected)

    def test_get_last_day_of_month(self):
        date = datetime(2020, 1, 15)
        result = Utils.get_last_day_of_month(date)
        expected = datetime(2020, 1, 31)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()