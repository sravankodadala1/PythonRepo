import unittest
from src.assignment6.util import String_formatting

class TestPrintFormatted(unittest.TestCase):
    def test_print_formatted(self):
        with self.assertRaises(SystemExit):
            String_formatting(5)

if __name__ == '__main__':
    unittest.main()
