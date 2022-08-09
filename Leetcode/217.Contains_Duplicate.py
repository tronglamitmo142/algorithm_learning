class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_num = {}
        for num in nums:
            if num in dict_num:
                dict_num[num] += 1 
            else:
                dict_num[num] = 1 
        for counter in dict_num.values():
            if counter == 1:
                continue 
            else:
                return True
            return False 
        