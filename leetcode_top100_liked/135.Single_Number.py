# https://leetcode.com/problems/single-number/ 
# O(n)

def main(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1 
        else:
            d[i] = 1
    for number, counter in d.items():
        if counter == 1: 
            return number

