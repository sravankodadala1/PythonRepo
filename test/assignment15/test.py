import unittest
from src.assignment15.util import word_order

class MyTestCase(unittest.TestCase):
    def test_something(self):
        words = ["mango", "apple", "banana", "mango"]
        count, occurrences = word_order(words)
        self.assertEqual(count, 3)
        self.assertEqual(occurrences, [2, 1, 1])



if __name__ == '__main__':
    unittest.main()
