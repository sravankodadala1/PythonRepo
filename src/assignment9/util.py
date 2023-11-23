from collections import namedtuple

def class_avg_marks(num_students, columns, student_data):
    total = 0
    Student = namedtuple('Student', columns)

    for i in student_data:
        student = Student(*i)
        total += int(student.marks)

    return total / num_students
