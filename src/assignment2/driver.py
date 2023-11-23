from util import total_marks
from src.assignment2.util import total_marks
  

n = int(input("Enter the number of students: "))
student_marks = {}

# Input student data
for i in range(n):
    name, *line = input("Enter student name and marks separated by space: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores

# Query for average percentage
query_name = input("Enter the name of the student to query: ")
total_marks(student_marks, query_name)


 
