from util import calculate_time_delta
import os
 
#input the number of test cases 
t = int(input("Enter the number of test cases: "))
#taking input of t1 and t2
for i in range(t):
    t1 = input("Enter the first time: ")
    t2 = input("Enter the second time: ")
    #calling the function
    delta = calculate_time_delta(t1, t2)

    print(delta)


