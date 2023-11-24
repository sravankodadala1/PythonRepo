import unittest
from src.assignment9.util import class_avg_marks

class MyTestCase(unittest.TestCase):
    def test_something(self): 
        num_students = 2
        columns = ['marks', 'classs', 'name', 'id']
        student_data = [['60', '4', 'khan', '1'],
                ['80', '4', 'krishna', '2']]

        result = class_avg_marks(num_students, columns, student_data)
        self.assertEqual(result, 70.0)



if __name__ == '__main__':
    unittest.main()
