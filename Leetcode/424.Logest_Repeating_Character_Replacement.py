class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    for element in p:
        count_p[element] = 1 + count_p.get(element, 0)
    while l < len(s):
        r = l + len(p)
        count_current = {}
        for element in s[l:r]:
            count_current[element] = 1 + count_current.get(element, 0)
            if count_p == count_current:
                res.append(l)
        l += 1
        return res
        
            
            
            
            