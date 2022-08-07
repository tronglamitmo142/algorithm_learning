def main(x, y, points):
    d_min = 100000
    for i in range(len(points)):
        if points[i][0] == x and points[i][1] == y:
            return i 
        elif points[i][0] == x or points[i][1] == y:
            d = abs(x-points[i][0]) + abs(y-points[i][1])
            if d < d_min:
                d_min = d
                res = i 
    if d_min == 100000:
        return -1 
    return res 

x = int(input())
y = int(input())
points =  list(list(map(int, input().split())))
print(main(x,y, points))