class Stack:
    def __init__(self):
        self.stack = []
    
    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True 
        else:
            return False
# Use peek to look at the top of the stack 
    def peek(self):
        return self.stack[-1]

# Use list pop method to remove elemnt
    def remove(self):
        if len(self.stack) <= 0: 
            return ("No element in the Stack")
        else:
            return self.stack.pop()
    
stack1 = Stack()
stack1.add("Mon")
stack1.add("Tue")
stack1.peek()
print(stack1.peek())
stack1.remove()
stack1.remove()
stack1.remove()

