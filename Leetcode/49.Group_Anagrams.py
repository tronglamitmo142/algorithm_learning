class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
# output = [["bat"],["nat","tan"],["ate","eat","tea"]]
        strs = sorted(strs, key=sorted)
        res = []
        current = [strs[0]] # bat
        for i in range(1, n):
            left = Counter(strs[i-1])
            right = Counter(strs[i])
            if left == right:
                current.append(strs[i])
            else:
                res.append(current)
                current = [strs[i]]
        res.append(current)
        return res
        