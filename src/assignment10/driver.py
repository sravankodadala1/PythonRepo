from util import calculate_time_delta
import os


t = int(input("Enter the number of test cases: "))

for i in range(t):
    t1 = input("Enter the first time: ")
    t2 = input("Enter the second time: ")

    delta = calculate_time_delta(t1, t2)

    print(delta)


