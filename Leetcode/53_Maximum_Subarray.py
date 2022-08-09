# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Input:[-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6 
# [4, -1, 2, 1] => Sum =6 
# Use Kanade's Algorithm 
# [-1]
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum =0 
        for n in nums:
            if curSum < 0:
                curSum = 0 
            curSum += n 
            maxSub = max(maxSub, curSum)
        return maxSub

a = Solution()
print(a.maxSubArray(['-1,-5,-4,2,5,1']))
