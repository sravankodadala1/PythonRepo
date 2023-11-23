import unittest
from src.assignment12.util import np_min_max

class MyTestCase(unittest.TestCase):
    def test_min_max(self):
        values = [
            [2, 1, 4],
            [5, 6, 7],
            [4, 7, 8]
        ]
        result = np_min_max(values)
        self.assertEqual(result, 7)



if __name__ == '__main__':
    unittest.main()
