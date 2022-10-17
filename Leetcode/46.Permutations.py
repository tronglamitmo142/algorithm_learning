class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(state, nums, res):
            if len(state) == len(nums):
                res.append(state[:])
                return
            for child in nums:
                if child not in state:
                    state.append(child)
                    dfs(state, nums, res)
                    state.pop()
        res = []
        dfs([], nums, res)
        return res