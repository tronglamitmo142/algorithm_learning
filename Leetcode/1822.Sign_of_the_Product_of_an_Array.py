def main(nums):
    product = 1 
    for num in nums:
        product *= num
    if product < 0:
        return -1 
    elif product > 0:
        return 1 
    return 0 

nums = list(map(int, input().split()))
print(main(nums))