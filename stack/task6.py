import queue
             
test_case = int(input())
for tc in range(test_case):
    n, t, m = map(int, input().split())
    q = []
    q.append(queue.Queue())
    q.append(queue.Queue())
    for id in range(m):
        car = input().split()
        if car[1] == 'left': 
            q[0].put((int(car[0]), id))
        else:
            q[1].put((int(car[0]), id))

    time = 0 
    side = 0 
    res = [0] * m

    while not q[0].empty() or not q[1].empty():
        if not q[0].empty() and not q[1].empty():
            nextTime = min(q[0].queue[0][0], q[1].queue[0][0])
        else:
            nextTime = q[0].queue[0][0] if not q[0].empty() else q[1].queue[0][0]
        
        time = max(time, nextTime)
        cnt = 0 
        while not q[side].empty():
            car, id = q[side].queue[0]
            if car <= time and cnt < n:
                cnt += 1 
                res[id] = time + t 
                q[side].get()
            else:
                break 
        time += t 
        side = 1 - side 

    for car in res: 
        print(car)
    if tc < test_case - 1:
        print()



        
    
