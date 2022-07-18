def main(k, n):
    count = 0 
    sum = 0
    n.sort(reverse=True)
    for i in range(len(n)):
        if sum < k:
            sum += n[i]
            count += 1 
        if sum < k and i == len(n) -1: 
            return -1 
    return count



k = int(input())
n = list(map(int, input().split()))
print(main(k, n))
