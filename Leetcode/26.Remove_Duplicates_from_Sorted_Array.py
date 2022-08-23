class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l, r  = 0, 0
        n = len(nums)
        while True:
            while r < n and nums[l] == nums[r]:
                r += 1 
            if r < n: 
                l += 1 
                nums[l] = nums[r]
            else:
                break
        return l + 1
        
nums = Solution()
print(nums.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

# i
# 0 0 1 1 1 2 2 3 3 4 
# l
