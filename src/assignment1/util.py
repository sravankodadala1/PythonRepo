from util import list_operations
from src.assignment1.util import list_operations
 
if __name__ == '__main__':
    N = int(input("Enter the number of commands: ")) 
    user_commands = [input().split() for i in range(N)]
    list_operations(user_commands)
