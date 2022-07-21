n, m = map(int, input().split())
 
q = []
time_free = 0
for _ in range(n):
    s, t = map(int, input().split())
 
    while q and q[0] <= s:
        q = q[1:]
 
    if s < time_free:
        if len(q) == m:
            print(-1)
        else:
            q.append(time_free)
            time_free += t
            print(time_free)
    else:
        time_free = max(time_free, s) + t
        print(time_free)