# https://leetcode.com/problems/search-insert-position/
# Complexity: O(logn)

def main(nums, target):
    left, right = 0, len(nums) - 1 
    while left <= right:
        mid = (left + right)//2
        if target < nums[mid]:
            right = mid -1 
        elif target > nums[mid]:
            left = mid + 1 
        else:
            return mid 
    return left
        

n = list(map(int, input().split()))
target = int(input())
print(main(n, target))

    