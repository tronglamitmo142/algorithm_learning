def main(nums):
    res = 0 
    check = True
    for num in nums:
        count = 0 
        while num > 0:
            num = num // 10 
            count += 1 
        if count % 2 == 0:
            res += 1 
    return res 

nums = list(map(int, input().split()))
print(main(nums))