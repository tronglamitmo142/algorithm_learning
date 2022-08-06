def main(x, y, points):
    res = []
    for point in point:
        if point[0] == x or point[1] == y:
            res.append[point]
    if len(res) == 0:
        return -1 
    else:
        distance_min = abs(res[0][0] - x) + abs[res[0][1] - y]
        for point in res:
            distance_cur = abs(point[0] - x) + abs([point[1] -y])
            distance_min = min(distance_min, distance_cur)
        if distance_min == 0:
            return 0 
        else: 
            


        






x = int(input())
y = int(input())
points =  list(list(map(int, input().split())))
