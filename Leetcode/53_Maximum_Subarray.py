# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Input:[-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6 
# [4, -1, 2, 1] => Sum =6 
# Use Kanade's Algorithm 
# [-1]
def main(nums):
    sum_now = 0 
    max_sum = 0 
    for num in nums: 
        sum_now += num
        if sum_now < 0:
            sum_now = 0  
        if sum_now > max_sum:
            max_sum = sum_now
    return max_sum

nums = list(map(int, input().split()))
print(main(nums))