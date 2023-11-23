import unittest
from src.assignment18.util import iterables_and_iterators

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertAlmostEqual(iterables_and_iterators(4, ['a', 'b', 'c', 'd'], 2), 0.5, places=3)



if __name__ == '__main__':
    unittest.main()
