# https://leetcode.com/problems/majority-element/
# O(n)

def main(nums):
    d = {}
    rs = 0 
    for i in nums: 
        if i in d: 
            d[i] += 1 
        else: 
            d[i] = 1 
    for element, value in d.items(): 
        if value > len(nums)/2:
            rs = element
            break 
    return rs 

nums = list(map(int, input().split()))
print(main(nums))