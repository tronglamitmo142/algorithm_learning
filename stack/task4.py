import queue

def main(n, queries):
    q_n = queue.Queue()
    # stack_e = []
    res = []
    for i in range(1,min(n, q)+ 1):
        q_n.put(i)
    for query in queries:
        if len(query) == 1:
            # if len(stack_e) > 0:
            #     res.append(stack_e.pop())
            # else:
            res.append(q_n.get())
            q_n.put(res[-1])
        else:
            x = int(query.split()[1])
            l = q_n.qsize()
            q_n.put(x)
            for i in range(l): 
                if q_n.queue[0] != x:
                    q_n.put(q_n.get())
                else:
                    q_n.get()
    return res
test_case = 1
while True:

    n, q = map(int, input().split())
    if n == 0 and q == 0:
        break
    queries = []
    for i in range(q):
        queries.append(input())
    print('Case {}:'.format(test_case))
    res = main(n, queries)
    for e in res:
        print(e)
    test_case += 1 
    


# cho n = min(n, q)  
