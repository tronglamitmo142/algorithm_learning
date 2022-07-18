def main(n,list_n, w):
    list_n.sort()
    return min(list_n[0], list_n[n+1-1]/2, w/3/n)*3*n

n, w = map(int, input().split())
list_n = list(map(int, input().split()))
print(main(n, list_n, w))

