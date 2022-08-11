import heapq 

def main(list_n):
    h = []
    res = []
    for i in range(len(list_n)):
        heapq.heappush(h, -list_n[i])
        if i < 2: 
            res.append(-1)
        else:
            max = []
            product = -1 
            for j in range(3):
                product *= h[0] 
                max.append(h[0])
                heapq.heappop(h)
            res.append(product)
            for j in range(3):
                heapq.heappush(h, max[j])
    return res 
n = int(input())
list_n = list(map(int, input().split()))
res = main(list_n)
for i in res:
    print(i)
