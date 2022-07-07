# Cho 2 mang A, B sap xep tang dan 
# Tao ra mang C gom cac phan tu A, B va co do lon tang dan 
# A: 1, 3, 6, 8, 10 
# B: 2, 6, 7, 12, 14, 15
def main(A, B):
    C = []
    i = 0 
    j = 0 
    while i < len(A) and j < len(B):
        print(i ,j)
        if A[i] < B[j]:
            C.append(A[i])
            i += 1 
        elif A[i] == B[j]:
            C.append(A[i])
            i += 1 
            j += 1 
        else: 
            C.append(B[j])
            j += 1 
    return C 

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(main(A, B))