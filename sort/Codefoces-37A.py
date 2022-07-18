# solution 
# Tim tan so xuat hien cua cac phan tu phan biet 
# Tim tan so lon nhat, Tim chieu dai 

def main(n):
    dict_number = {}
    for number in n:
        if number in dict_number:
            dict_number[number] += 1 
        else:
            dict_number[number] = 1 
    
    return max(dict_number.values()), len(dict_number)

n = int(input())
list_n = list(map(int, input().split()))
max_tower, number_tower = main(list_n)
print(max_tower, number_tower)

