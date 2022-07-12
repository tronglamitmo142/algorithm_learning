# Khoảng không đổi: Các phần tử trong mảng hơn kém nhau nhiều nhất là 1 đơn vị 
# Codeforce 602B 
# Counting sort 
def check(diff):
    return len(diff) <= 1 or (len(diff) == 2 and abs(diff[0] - diff[1]) == 1)

def const_list(n, list_n):
    start = 0 
    res = 0
    count = [0]*(max(list_n)+1)
    diff = []

    for end in range(len(list_n)):
        if count[list_n[end]] == 0: 
            diff.append(list_n[end]) 
        count[list_n[end]] += 1
        while start <= end and check(diff) == False: 
            count[list_n[start]] -= 1
            if count[list_n[start]] == 0:
                diff.remove(list_n[start])
            start += 1 
        res = max(res, end - start + 1)
    return res 
        
N = int(input())
list_n = list(map(int, input().split()))
print(const_list(N, list_n))

# N = [1,2,3,3,2]
# print(max(N[1:3]))