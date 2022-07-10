# Khoảng không đổi: Các phần tử trong mảng hơn kém nhau nhiều nhất là 1 đơn vị 

from itertools import count


def const_list(list_n):
    count_death = 0 
    i = len(list_n) - 1
    while i > 0:
        i = i - list_n[i]
        count_death += list_n[i]
        print(count_death)
    
    
     
        

    return const_list

N = input()
list_n = list(map(int, input().split()))
const_list(list_n)