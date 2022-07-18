# check doan giam dan dai nhat va duy nhat 
# check 2 dau mut 
def main(n, list_n):
    i = 1 
    while i < n and list_n[i] >= list_n[i-1]:
        i += 1 
    j = 1 
    while j < n and list_n[j] <= list_n[j-1]:
        j += 1 
    check_list = list_n[:i-1] + list_n[i-1:j][::-1] + list_n[j:]
    list_n.sort()
    if check_list == list_n:
        print("yes")
        print(i, j)
    else:
        print("no")



    
