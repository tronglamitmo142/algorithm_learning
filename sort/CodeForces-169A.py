def main(chores, a, b):
    chores.sort()
    return chores[b] - chores[b-1]

n, a, b = map(int, input().split())
chores = list(map(int, input().split()))
print(main(chores, a, b))
