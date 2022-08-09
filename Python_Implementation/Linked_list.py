# Linked list is a sequence of data element, which are conected via the links.
# Each data element contains a conection to another data element in form of a pointer 

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval 
        self.nextval = None 

class SLinkedList:
    def __init__(self):
        self.headval = None 

# traversing a linked list 
    def listprint(self):
        printval = self.headval
        while printval is not None: 
            print(printval.dataval)
            printval = printval.nextval 

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# link first node to second node 
list1.headval.nextval = e2 
# link second node to third node
e2.nextval = e3 
list1.listprint()