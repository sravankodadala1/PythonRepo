import numpy as np

def mean_var_std(n, m, data):
    k = np.array(data, dtype=int)
    np.set_printoptions(legacy='1.13')
    print(np.mean(k, axis=1), np.var(k, axis=0), np.std(k), sep='\n')

