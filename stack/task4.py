import queue

def main(n, queries):
    q_n = queue.Queue()
    res = []
    save_x = []
    for i in range(1, n+1):
        q_n.put(i)
    for query in queries:
        while q_n.queue[0] in save_x:
            save_x.remove(q_n.get())
        if len(query) == 1:
            res.append(q_n.get())
            q_n.put(res[-1])
        else:
            x = int(query.split()[1])
            q_n.put(x)
            save_x.append(x)
    return res
        
while True:

    n, q = map(int, input().split())
    if n == 0 and q == 0:
        break
    queries = []
    for i in range(q):
        queries.append(input())
    print(main(n, queries))

# cho n = min(n, q)  
