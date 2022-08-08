from array import*

T =[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print(T[0])

# print matrix
for r in T: 
    for c in r:
        print(c, end = " ")
    print()

# Inserting Values 
T.insert(2, [0, 0, 0, 0])
for r in T: 
    for c in r:
        print(c, end = " ")
    print()

# Update by Indexing 
T[2] = [11, 9]
T[0][3] = 7 

# Deleting by index
del T[3]
