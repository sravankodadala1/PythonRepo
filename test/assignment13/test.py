import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        values = numpy.array([[2..0, 3.0], [4.0, 5.0]])
        result = linear_algebra(values)
        self.assertEqual(result, -2.0)



if __name__ == '__main__':
    unittest.main()
