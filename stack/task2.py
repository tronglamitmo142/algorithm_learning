import queue
def main(cars):
    q_car = queue.Queue()
    s_car = []
    count = 1

    for car in cars:
        q_car.put(car)
    while True: 
        if len(s_car) > 0 and s_car[-1] == count:
            s_car.pop()
            count += 1 
        else: 
            while q_car.qsize() > 0 and q_car.queue[0] != count:
                s_car.append(q_car.get())
            if q_car.qsize() > 0:
                q_car.get()
                count += 1 
        if count == len(cars) + 1:
            return "yes"
        if q_car.empty() and s_car[-1] != count:
            break 
    return "no"

while True:
    n = int(input())
    if n == 0:
        break 
    cars = list(map(int, input().split()))
    print(main(cars))




