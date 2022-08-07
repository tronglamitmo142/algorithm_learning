class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]
        visited = [False for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def DFS(u):
            visited[u] = True
            for v in graph(u):
                if not visited(v):
                    DFS(v)
        DFS(source)
        return visited[destination]

