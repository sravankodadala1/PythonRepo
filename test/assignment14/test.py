import unittest
from src.assignment14.util import happiness

class MyTestCase(unittest.TestCase):
    def test_something(self):
        array_values = [2,3,4,5,6,7,8]
        a = {3,1,1}
        b = {3,1,10}
        result = happiness(array_values, a, b)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
