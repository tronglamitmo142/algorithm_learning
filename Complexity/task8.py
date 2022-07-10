#Codeforce 6C 
from itertools import count


def main(n, list_n):
    time_a, time_b = 0, 0 
    count_a, count_b = 0, 0 
    i, j = 0, n-1 
    while i <= j: 
        if time_a <= time_b: 
            time_a += list_n[i]
            count_a += 1 
            i += 1 
        else:
            time_b += list_n[j]
            count_b += 1 
            j -= 1 
    return count_a, count_b 

n = int(input())
list_n = list(map(int, input().split()))
count_a, count_b = main(n, list_n)
print(count_a, count_b)

        
        