import unittest
from src.assignment3.util import Runner_up_score
class TestUtilFunctions(unittest.TestCase):
    def test_get_second_largest(self):
        n = 5
        arr = [2, 3, 6, 6, 5]
        result = Runner_up_score(n, arr)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()
