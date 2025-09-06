import unittest
from datetime import datetime, timedelta, timezone
from src.utils.time_utils import get_time_range

class TestTimeUtils(unittest.TestCase):

    def test_24h(self):
        start, end = get_time_range("24h")
        end_dt = datetime.fromisoformat(end)
        start_dt = datetime.fromisoformat(start)
        delta = end_dt - start_dt
        self.assertTrue(abs(delta - timedelta(hours=24)) < timedelta(seconds=1))

    def test_7d(self):
        start, end = get_time_range("7d")
        end_dt = datetime.fromisoformat(end)
        start_dt = datetime.fromisoformat(start)
        delta = end_dt - start_dt
        self.assertTrue(abs(delta - timedelta(days=7)) < timedelta(seconds=1))

    def test_30d(self):
        start, end = get_time_range("30d")
        end_dt = datetime.fromisoformat(end)
        start_dt = datetime.fromisoformat(start)
        delta = end_dt - start_dt
        self.assertTrue(abs(delta - timedelta(days=30)) < timedelta(seconds=1))

    def test_90d(self):
        start, end = get_time_range("90d")
        end_dt = datetime.fromisoformat(end)
        start_dt = datetime.fromisoformat(start)
        delta = end_dt - start_dt
        self.assertTrue(abs(delta - timedelta(days=90)) < timedelta(seconds=1))

    def test_invalid_option(self):
        with self.assertRaises(ValueError):
            get_time_range("1y")

if __name__ == "__main__":
    unittest.main()
