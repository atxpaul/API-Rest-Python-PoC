import unittest
from app.services.time_service import get_current_time


class TimeServiceTestCase(unittest.TestCase):
    def test_get_current_time(self):
        current_time = get_current_time()

        self.assertIsNotNone(current_time)
        self.assertIsNotNone(current_time.time_string)
        self.assertIsNotNone(current_time.timezone)


if __name__ == '__main__':
    unittest.main()
