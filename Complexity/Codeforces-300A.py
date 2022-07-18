# [L, R] chứa đúng K phần tử phân biệt
# [L,R] Không có đoạn nào cũng chứa K phần tử phân 

def main(K, list_n):
    count = [0]*(100000+1)
    unique = 0 
    # giai dieu kien 1: 
    for i in range(len(list_n)):
        if count[list_n[i]] == 0:
            unique += 1 
        count[list_n[i]] += 1 
        if unique == K: # thoa dieu kien 1
            j = 0 
            while True:
                if count[list_n[j]] > 1:
                    count[list_n[j]] -= 1
                    j += 1 
                else:
                    return j+1, i+1
    return -1, -1

N, K = map(int, input().split())
list_n = list(map(int, input().split()))
L, R = main(K, list_n)
print(L, R)




    
