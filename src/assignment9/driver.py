from util import class_avg_marks


num_students = int(input("enter number of students"))
columns = input("enter total fields").split()

student_data = [input().split() for i in range(num_students)]

avg_marks = class_avg_marks(num_students, columns, student_data)
print('{:.2f}'.format(avg_marks))
