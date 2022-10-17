class Node:
    def __init__(self, val):
        self.left = None 
        self.right = None 
        self.val = val 
    def printVal(self):
        print(self.val)

root = Node(10)
root.printVal()