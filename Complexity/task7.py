# Codeforce 892B 
from itertools import count


def main(list_n):
    count = 0 
    i = len(list_n) - 1 
    while i > 0:
        i = i - list_n[i]
        count += list_n[i]
        print(count)

N = input()
list_n = list(map(int, input().split()))
main(list_n)