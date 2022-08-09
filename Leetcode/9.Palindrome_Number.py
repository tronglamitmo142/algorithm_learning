class Solution:
 # O(log(n): 
    def isPalindrome(self, x: int) -> bool:
    #     str_x = str(x)
    #     n = len(str_x) - 1 
    #     left = 0 
    #     right = n
    #     check = True
    #     while left <= right: 
    #         if str_x[left] == str_x[right]:
    #             left += 1 
    #             right -= 1 
    #         else:
    #             check = False
    #             break 
    #     return check
# O(1):
        if x < 0: 
            return False 
        x = str(x)
        n = len(x)
        m = n//2 
        if n%2 == 0: 
            if x[m:][::-1] == x[:m]:
                return True
            else:
                return False
        else:
            if x[m+1:][::-1] == x[:m]:
                return True 
            else:
                return False 

a = Solution()
print(a.isPalindrome(121))
