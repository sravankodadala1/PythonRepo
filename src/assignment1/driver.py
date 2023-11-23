def list_operations(commands):
    list = []

    for com in commands:
        if com[0] == "insert":
            list.insert(int(com[1]),int(com[2]))
        elif com[0] == "print":
            print(list)
        elif com[0] == "remove": 
            e = int(com[1])
            list.remove(e)
        elif com[0] == "append":
            e = int(com[1])
            list.append(e)
        elif com[0] == "sort":
            list.sort()
        elif com[0] == "pop":
            list.pop()
        elif com[0] == "reverse":
            list = list[::-1]

    return list 
