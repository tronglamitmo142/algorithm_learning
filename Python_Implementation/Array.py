# Array is container which can hold a fix number of items and these items should be of the same type
# 2 important temrm: Element, Index
# Basic Operations:
# Traverse: Print all the array element one by one
# Insertion: Adds an element at the given index
# Deletion: Deletes an element at the given index
# Search: Searches an element using given index or by value
# Update: Update an elemnt at the given index 

from array import *

array1 = array('i', [10, 20, 30, 40, 50])

# Print all value:
for x in array1:
    print(x)

# Accessing Array Element by Index: 
print(array1[0])

# Insert by Index: 
array1.insert(1, 60)
for x in array1:
    print(x)

# Delete: 
array1.remove(40)

# Search index of specify value 
array1.index(10)

# Update value by index
array1[2] = 80 
print(array1)

