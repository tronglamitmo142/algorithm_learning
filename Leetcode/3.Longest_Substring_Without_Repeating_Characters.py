class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # Create a dictionary to keep track the unique element by index 
        l = 0 # left pointer
        output = 0 
        for r in range(len(s)):
            if s[r] not in seen: # If s[r] not in seen, we can keep moving the right pointer 
                output = max(output, r-l+1)
            else:
                if seen[s[r]] < l:
                    output = max(output, r-l+1)
                else:
                    l = seen[s[r]] + 1 
            seen[s[r]] = r 
        return output
s = 'acbdbacd'        
a = Solution()
a.lengthOfLongestSubstring(s)
print(a)