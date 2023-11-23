import unittest
from src.assignment19.util import filter_and_sort_emails,is_valid_email

class MyTestCase(unittest.TestCase):
    def test_something(self):
        def test_is_valid_email(self):
            self.assertTrue(is_valid_email("john_doe@example.com"))


        def test_filter_and_sort_emails(self):
            emails = ["john_doe@example.com", "user123@example.co.in", "not_an_email", "user@.com", "user@.co.in"]
            result = filter_and_sort_emails(emails)
            expected_result = ["john_doe@example.com", "user123@example.co.in"]
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
