# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/ 
# O(1)
# Array, Sorting 

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 1 or low % 2 == 1:
            return (high-low)//2 + 1 
        else: 
            return (high-low)//2 
