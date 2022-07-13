from itertools import count

def check(N, list_n):
    if N == 1: #check specific senario 
        if list_n[0] == 1:
            return "YES"
        return "NO"
    else:
        for i in list_n:
            count = 0 # count so nut ao open 
            if list_n[i] == 1:
                continue
        else: 
            count += 1 
        if count == 1:
            return "YES"
        return "NO"

N = int(input())
list_n = list(map(int, input().split()))
print(check(N, list_n))
