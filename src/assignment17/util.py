def Pilling_up(lst):
    min_index = lst.index(min(lst))
    left = lst[:min_index]
    right = lst[min_index + 1:]
 
    return left == sorted(left, reverse=True) and right == sorted(right)
