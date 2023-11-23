from src.assignment3.util import Runner_up_score

#user input the number of participants
n = int(input("Enter the number of participants "))
#enter the values for participants
arr = list(map(int, input("enter participants seperated by space").split()))
#calling the function and storing it in result
result = Runner_up_score(n, arr)
print("Score of runner-up", result)
