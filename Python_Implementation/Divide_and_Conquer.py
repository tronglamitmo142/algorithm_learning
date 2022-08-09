# 3 steps
# Divide 
# Conquer/solve
# Merge 
# Binary search implementation 

def bsearch(list, val):
    list_size = len(list) - 1 
    left = 0 
    right = list_size

# Find the middle most value 
    while left <= right:
        mid = (left+right) // 2 
        if list[mid] == val:
            return mid 

# Compare the value the middle most value 
    if val > list[mid]:
        left = mid + 1 
    else:
        right = mid - 1 
    if left > right:
        return None 

list1 = [2,3,4,5,6,10]
print(bsearch(list1, 10))