import unittest
from PythonRepo.src.assignment4.util import mutate_string

class MyTestCase(unittest.TestCase):
    def test_something(self):

        output=mutate_string("abcd", 2, "a")
        self.assertEqual(output, "abad")

 
if __name__ == '__main__':
    unittest.main()
