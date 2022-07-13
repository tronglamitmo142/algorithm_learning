def main(N, left, right):
    min_left = min(left)
    max_right = max(right)
    for i in range(N):
        if left[i] == min_left and right[i] == max_right:
            return i+1 
    return -1 

N = int(input())
left = [0]*N
right =[0]*N
for i in range(N):
    left[i], right[i] = map(int, input().split())
print(main(N, left, right))
        



# [A, B]
