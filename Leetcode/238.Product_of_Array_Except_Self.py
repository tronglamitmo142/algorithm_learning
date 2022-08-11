class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # 1 1 2 6 
        postfix = 1 
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        # 24 12 4 1 
        return res

a = Solution()
nums = list(map(int, input().split()))
print(a.productExceptSelf(nums))
