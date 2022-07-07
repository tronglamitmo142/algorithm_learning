# Given a sorted array A (sorted in ascending order), having N integers, find
# if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.
# A[] = [10, 20, 35, 50, 75, 80]
# X = 70

def check(A, X):
    i = 0 
    j = len(A) - 1 
    check = False 
    while i < j:
        if A[i] + A[j] == X:
            check = True
            break
        if A[i] + A[j] > X:
            j = j-1 
        if A[i] + A[j] < X:
            i = i + 1 
    return check

A = list(map(int, input().split()))
X = int(input())
print(check(A, X))
