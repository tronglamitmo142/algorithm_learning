import queue
def main(n):
    q_n = queue.Queue()
    discard = []
    for i in range(1, n+1):
        q_n.put(i)
    while q_n.qsize() > 1: 
        discard.append(q_n.get())
        q_n.put(q_n.get())
    remain = q_n.get()
    return discard, remain

while True:
    n = int(input())
    if n == 0:
        break 
    discard, remain = main(n)
    print("Discarded cards:", end="")
    if len(discard) > 0:
        print(" " + str(discard)[1:-1])
    else: 
        print()
    print("Remaining card: {}".format(remain))

    
    

