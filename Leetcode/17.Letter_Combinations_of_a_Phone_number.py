class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':['a','b','c'],
                  '3':['d','e','f'],
                  '4':['g','h','i'],
                  '5':['j','k','l'],
                  '6':['m','n','o'],
                  '7':['p','q','r','s'],
                  '8':['t','u','v'],
                  '9':['w','x','y','z']}
        res = []
        def dfs(pos, state):
            if (pos == len(digits)):
                if state:
                    res.append("".join(state))
                return
            for letter in mapping[digits[pos]]:
                state.append(letter)
                dfs(pos+1, state)
                state.pop()
        dfs(0, [])
        return res