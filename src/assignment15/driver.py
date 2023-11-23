from util import word_order



n = int(input("enter the number of words"))
words = [input("enter the word") for i in range(n)]

count, occurrences = word_order(words)

print(count)
print(*occurrences, end=" ")


