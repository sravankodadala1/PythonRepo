import unittest
from src.assignment10.util import calculate_time_delta

class MyTestCase(unittest.TestCase):
    def test_something(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"

        result = calculate_time_delta(t1, t2)
        self.assertEqual(result, "25200")



if __name__ == '__main__':
    unittest.main()
