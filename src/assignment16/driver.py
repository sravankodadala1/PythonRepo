import numpy as np
 
from util import mean_var_std

if __name__ == "__main__":
    n, m = map(int, input("Enter the number of rows and columns: ").split())
    data = [input().split() for _ in range(n)]

    mean_var_std(n, m, data)
