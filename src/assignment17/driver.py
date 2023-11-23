from util import Pilling_up

 
test_cases = int(input("Enter number of test cases: "))

for i in range(test_cases):
    input()  
    numbers = [int(num) for num in input("Enter space-separated numbers: ").split()]

    if Pilling_up(numbers):
        print("Yes")
    else:
        print("No")
