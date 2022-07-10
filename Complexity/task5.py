def main(N):
    i = 0 
    j = len(N) - 1 
    person = 0 # person 0: A, person 1: B 
    sum = [0]*2
    while i <= j:
        if N[i] > N[j]:
            sum[person] += N[i]
            i += 1 
        else: 
            sum[person] += N[j]
            j -= 1   
        person = 1 - person 
    return sum 

input()
N = list(map(int, input().split()))
A, B = main(N)
print(A, B)
        
        

        