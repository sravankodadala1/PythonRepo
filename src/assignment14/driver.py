from util import happiness

#user input the values for array
array_values = list(map(int, input("enter the values of array").split()))
#user input the values for set1
a = set(map(int, input("enter the values of set1").split()))
#user input the values for set2
b = set(map(int, input("enter the values of set2").split()))
#calling the function
result = happiness(array_values, a, b)
print(result)




