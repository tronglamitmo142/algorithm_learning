class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # count = 0
        # for i in range(n):
        #     sum = nums[i]
        #     if sum == k:
        #         count += 1 
        #     for j in range(i+1, n):
        #         sum += nums[j]
        #         if sum == k:
        #             count += 1 
        slow, fast = 0, 0 
        count = 0 
        while fast < n:
            sum = nums[slow]
            fast += 1 
            nums += 
        return count

nums = Solution()
print(nums.subarraySum([1,2,3], 3))