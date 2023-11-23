def happiness(array, a, b):
    #initialize happiness as 0
    happiness = 0
    for i in array:
        #if value of i in set1, increment happiness by 1
        if i in a:
            happiness += 1
        #if value of i in set2, decrement happiness by 1
        elif i in b:
            happiness -= 1
    #return the values of happiness
    return happiness
