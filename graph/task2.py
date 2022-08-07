import queue
 
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
 
def isValid(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m
 
def BFS(a, s, f):
    n = len(a)
    m = len(a[0])
    q = queue.Queue()
 
    visited[s.x][s.y] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for i in range(4):
            v = Node(u.x + dx[i], u.y + dy[i])
            if isValid(v) and a[v.x][v.y] == '.':
                q.put(v)
                visited[v.x][v.y] = True
            if not isValid(v):
                border += 1
    return visited[f.x][f.y]
# def BFS(s):
#     q = queue.Queue()
#     visited[s.x][s.y] = True
#     q.put(s)
#     border = 0
#     while not q.empty():
#         u = q.get()
#         isBorder = False
#         for i in range(4):
#             v = Node(u.x + dx[i], u.y + dy[i])
#             if isValid(v) and a[v.x][v.y] == '.':
#                 q.put(v)
#                 visited[v.x][v.y] = True
#             if not isValid(v):
#                 isBorder = True
#         border += isBorder
#     return border
 
def ValidateTheMaze():
    open = []
    for i in range(n):
        if a[i][0] == '.':
            open.append(Node(i, 0))
        if m > 1 and a[i][m - 1] == '.':
            open.append(Node(i, m - 1))
    for i in range(1, m - 1):
        if a[0][i] == '.':
            open.append(Node(0, i))
        if n > 1 and a[n - 1][i] == '.':
            open.append(Node(n - 1, i))
    if len(open) != 2:
        return 'invalid'
    s, f = open
    if BFS(a, s, f):
        return 'valid'
    else:
        return 'invalid'
    # sumBorder = 0
    # for i in range(n):
    #     for j in range(m):
    #         if a[i][j] == '.' and not visited[i][j]:
    #             border = BFS(Node(i, j))
    #             if border != 2 and border != 0:
    #                 return 'invalid'
    #             sumBorder += border
    # return sumBorder == 2
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    visited = [[False for j in range(m)] for i in range(n)]
    a = []
    for i in range(n):
        a.append(input())
    print(ValidateTheMaze(a))