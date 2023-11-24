import unittest
from PythonRepo.src.assignment5.util import updated_string

class MyTestCase(unittest.TestCase):
    def test_something(self): 
        string="ABACAACDC"
        k=3
        result=updated_string(string, k)
        self.assertEqual(result,"AB\nCA\nCD\n")  # add assertion here


if __name__ == '__main__':
    unittest.main()
