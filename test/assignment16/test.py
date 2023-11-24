import unittest
from src.assignment16.util import mean_var_std  

class MyTestCase(unittest.TestCase):
    def test_something(self):
        values = [[1, 2, 3], [4, 5, 6]]
        expected_output = ["2.0", "2.25", "2.0"]
        actual_output = []
        original_print = print
        print = lambda *args: actual_output.extend(map(str, args))
        mean_var_std(2, 3, values)
        print = original_print
        self.assertEqual(actual_output, expected_output)



if __name__ == '__main__':
    unittest.main()
