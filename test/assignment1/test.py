
import unittest
from src.assignment1.util import list_operations

class TestListCommands(unittest.TestCase): 
    def test_list_operations(self):
        # Example test case
        l1 = []
        commands = [['insert', '1', '7'], ['insert', '1', '3'], ['append','5'], ['print']]
        output =[7,3,5]
        result = list_operations(commands)
        self.assertEqual(result,output)

if __name__ == '__main__':
    unittest.main()
