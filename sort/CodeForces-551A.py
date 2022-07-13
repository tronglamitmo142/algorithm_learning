# GukiZ and Contest 
# Solution: Find the numbers of element greateer than => + 1 in sum 

def main(n):
    res = []
    count = 0 
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] < n[j]:
                count += 1 
        if j == len(n) -1:
            res.append(count+1)
            count = 0 
    return res 

N = int(input())
list_n = list(map(int, input().split()))
res = main(list_n)
[print(i, end=' ') for i in res ]