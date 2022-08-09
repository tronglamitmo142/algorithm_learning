class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n 
        while True: 
            mid = (left+right) // 2 
            if guess(mid) == -1:
                right = mid - 1 
            elif guess(mid) == 1:
                left = mid + 1 
            else:
                return mid 