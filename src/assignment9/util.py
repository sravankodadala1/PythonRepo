from collections import namedtuple

def class_avg_marks(num_students, columns, student_data):
    
    total = 0
    #creating a namedtuple
    Student = namedtuple('Student', columns)
    
    for i in student_data:
        #assigning each element of list to corresponding field of named tuple
        student = Student(*i)
        #adding the marks of students
        total += int(student.marks)
    #return average marks of students
    return total / num_students
