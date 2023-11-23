def updated_string(string, k):
    #initialize c to 0
    c = 0
    #created a empty string
    sub_string = ""
    result=""

    for i in string:
        #if i not present in sub_string increment sub_string by 1
        if i not in sub_string:
            sub_string = sub_string + i
        c = c + 1
        if c == k:
            #assigning values of substring to result
            result += sub_string + "\n"
            c = 0
            sub_string = ""
    return result