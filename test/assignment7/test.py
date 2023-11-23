import unittest
from src.assignment7.util import get_day_of_week

class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = get_day_of_week(11, 22, 2023)
        self.assertEqual(result, 'Wednesday')

if __name__ == '__main__':
    unittest.main()
