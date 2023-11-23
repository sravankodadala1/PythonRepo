def mutate_string(string, position, character):
    #converting the values into list
    a=list(string)
    #assigning character at given position index
    a[position]=character
    #joining the list values and making it a list
    string=''.join(a)
    return string

