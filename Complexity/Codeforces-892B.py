# Codeforce 892B 


def main(list_n):
    j = 0
    count = 0 
    last_kill = len(list_n) - 1 
    for i in range(len(list_n) - 1, -1, -1):
        last_kill = min(last_kill, i)
        j = max(0, i - list_n[i])
        if j < last_kill:
            count += last_kill - j 
            last_kill = j 
    return len(list_n)-count 

N = input()
list_n = list(map(int, input().split()))
print(main(list_n))