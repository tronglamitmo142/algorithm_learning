# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# O(n)

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1])/(len(salary)-2)