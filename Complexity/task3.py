# Dem so phan tu trong list => find subaaray with max length 

def main(T, list_n):
    subarray_start = 0 
    subarray_end = 0 
    subarray_sum = 0 
    max_len = 0 
    for i in list_n: 
        subarray_sum += i 
        subarray_end += 1 
        while subarray_sum > T:
            subarray_sum -= list_n[subarray_start]
            subarray_start += 1 
        if subarray_sum <= T:
            max_len = max(max_len, subarray_end - subarray_start)
    
    return max_len




N, T = map(int, (input().split()))
books = list(map(int, input().split()))
print(main(T, books))