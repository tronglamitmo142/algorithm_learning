class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0 
        right = num // 2
        if num == 1:
            return True
        else:
            while left <= right:
                mid = (left+right) // 2 
                if mid == num:
                    return True 
                elif mid < num:
                    left = mid + 1 
                else:
                    right = mid - 1 
a = Solution()
num = int(input())
print(a.isPerfectSquare(num))