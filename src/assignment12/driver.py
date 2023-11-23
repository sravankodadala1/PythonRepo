from util import np_min_max


n, m = map(int, input().split())
array = [list(map(int, input().split())) for i in range(n)]
result = np_min_max(matrix)
print(result)

 
