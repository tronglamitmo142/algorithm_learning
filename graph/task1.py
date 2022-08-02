import queue

def BFS(graph, s):
    n = len(graph)
    visited = [False for i in range(n)]
    dist = [-1 for i in range(n)]
    q = queue.Queue()
    q.put(s)
    visited[s] = True 
    dist[s] = 0 
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                q.put(v) 
                visited[v] = True
                dist[v] = dist[u] + 6 
                
    return dist

q = int(input())
for _ in range(q):
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        
    s = int(input()) - 1 
    dist = BFS(graph, s)
    for x in dist:
        if x != 0:
            print(x, end=' ')
    print()
