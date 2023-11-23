import unittest
from src.assignment17.util import Pilling_up

class MyTestCase(unittest.TestCase):
    def test_something(self):

        self.assertTrue(Pilling_up([1, 2, 3, 4, 5]))

if __name__ == '__main__':
    unittest.main()
