from itertools import combinations

def iterables_and_iterators(N, L, K):
    C = list(combinations(L, K))
    F = filter(lambda c: 'a' in c, C)
    probability = len(list(F)) / len(C)
    return round(probability, 3)
