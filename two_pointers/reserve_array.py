# reserve array 
# Input: [10, 20, 40, 50, 70]
# Output:[ 70, 50, 40, 20, 10]

def reserve_array(A):
    i = 0 
    j = len(A) - 1 
    while i < j: 
        A[i], A[j] = A[j], A[i]
        i += 1 
        j -= 1 
    return A 

A = list(map(int, input().split()))
print(reserve_array(A))