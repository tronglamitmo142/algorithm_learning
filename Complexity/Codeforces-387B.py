def main(N, M):
    j = 0 
    for i in range(len(N)):
        while j < len(M) and M[j] < N[i] : # And xu ly DK 1 truoc  -> DK 2 
            j += 1 
        if j == len(M):
            return len(N) - i 
        else: 
            j += 1 
    return 0 

N, M = map(int, input().split())
list_N = list(map(int, input().split()))
list_M = list(map(int, input().split()))
print(main(list_N, list_M))






