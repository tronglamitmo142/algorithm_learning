import heapq

h = []
h2 = []
n = int(input())
for i in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(h, query[1])
    elif query[0] == 2:
        heapq.heappush(h2, query[1])
    elif query[0] == 3:
        while len(h2) > 0 and h[0] == h2[0]:
            heapq.heappop(h)
            heapq.heappop(h2)
        print(h[0])



