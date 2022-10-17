class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     store = {}
    #     for index, value in enumerate(nums):
    #         if target - value in store:
    #             return [value, target - value]
    #         store[value] = index

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        index = {}
        res = []
        for k in range(len(nums)):
            index[nums[k]] = k
        for x in range(len(nums) - 2):
            for y in range(x + 1, len(nums) - 1):
                value = 0 - nums[x] - nums[y]
                k = index.get(value)
                if index.get(value) != None:
                    if y < k:
                        res.append((nums[x], nums[y], nums[k]))
        return list(set(res))


