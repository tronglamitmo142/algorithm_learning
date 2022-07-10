# Khoảng không đổi: Các phần tử trong mảng hơn kém nhau nhiều nhất là 1 đơn vị 
# Codeforce 602B 

def const_list(n, list_n):
    i = 0 
    j = 1 
    count = 0 
    max_list = 0 
    while j < n:
        distance = max(list_n[i:j+1]) - min(list_n[i:j+1])
        if distance <= 1: 
            j += 1 
        else: 
            i += 1 

    
    print(i, j, list_n[i:j+1])
    return len(list_n[i:j+1])
        


N = input()
list_n = list(map(int, input().split()))
print(const_list(5, list_n))

# N = [1,2,3,3,2]
# print(max(N[1:3]))