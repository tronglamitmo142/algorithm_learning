class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0 
        r = 1 
        n = len(s)
        for r in range(n):
            while s[r] in s[l:r]:
                l += 1 
            res = max(res, r-l+1)
        return res

s = 'acbdbacd'        
a = Solution()
a.lengthOfLongestSubstring(s)
print(a)