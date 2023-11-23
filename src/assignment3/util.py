def Runner_up_score(n, arr):
    #conver the arr into string and sorted
    runner_up = sorted(set(arr))
    #return the second last value 
    return runner_up[-2]
