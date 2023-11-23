from util import class_avg_marks

#enter the number of students
num_students = int(input("enter number of students"))
#enter the number of fields 
columns = input("enter total fields").split()
#input the student fields
student_data = [input("enter the student fields").split() for i in range(num_students)]
#calling the function
avg_marks = class_avg_marks(num_students, columns, student_data)
print('{:.2f}'.format(avg_marks))
 
