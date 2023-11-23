from util import mutate_string
 
#enter the string
s = input("enter the string")
#enter the postion and character where you want to change
p, c = input("enter the postion and character seperated by a space").split()
#calling the function and assigned it to updated_string
updated_string = mutate_string(s, int(p), c)
print(updated_string) 
