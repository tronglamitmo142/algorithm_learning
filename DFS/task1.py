n = int(input())
graph = [[] for i in range(n)]
visited = [False for i in range(n)]
dist = [0 for i in range(n)] # Luu lai khoang cach tu 1 -> cac nuoc khac 
for i in range(n-1):
    u, v = map(int, input().split())
    u -= 1 
    v -= 1 
    graph[u].append(v)
    graph[v].append(u)
def DFS(u):
    visited[u] = True 
    for v in graph[u]:
        dist[v] = dist[u] + 1 
        if not visited[v]:
            DFS(v)

dist[1] = 0
DFS(1) 

q = int(input())
minDist, minGirl = n, n 
for i in range(q):
    girl = int(input())
    if dist[girl] == minDist and girl < minGirl:
        minGirl = girl
    if dist[girl] < minDist:
        minDist = dist[girl]
        minGirl = girl

print(minGirl) 