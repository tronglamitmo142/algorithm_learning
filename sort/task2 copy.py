# check doan giam dan dai nhat va duy nhat 
# check 2 dau mut 

def main(n):
    check = False
    max_sub_string = 0
    start = 0
    for start in range(len(n)):
        end = start + 1 
        while n[end] < n[start]: # doan giam dan
            end += 1 


        
