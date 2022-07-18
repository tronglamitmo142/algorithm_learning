def main(N, M, X, Y):
    list_res = []
    j = 0
    for i in range(len(N)):
        while j < len(M) and M[j] < N[i] - X: 
            j += 1 
        if j == len(M):
            break 
        if M[j] <= N[i] + Y: 
            list_res.append([i+1, j+1])
            j += 1 
    return list_res

N, M, X, Y = map(int, input().split())
list_N = list(map(int, input().split()))
list_M = list(map(int, input().split()))
res = main(list_N, list_M, X, Y)
print(len(res))
for N in res: 
    print(N[0], N[1])

        
        
        

