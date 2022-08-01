# Tim K phan tu nho nhat cua A 
# M phan tu lon nhat cua B 
# so sanh K max va M min

def main(A, B, k, m):
    max_A = A[k-1]
    min_B = B[len(B) - m]
    if max_A > min_B:
        return "NO"
    return "YES"

size = input()
k, m = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

print(main(A, B, k, m))

