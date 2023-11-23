from util import iterables_and_iterators

 
A = int(input("Enter the total number of elements: "))
L = input("Enter space-separated elements: ").split()
K = int(input("Enter the combination size: "))

result = iterables_and_iterators(A, L, K)
print(f"The probability of a combination containing 'a' is: {result}")
