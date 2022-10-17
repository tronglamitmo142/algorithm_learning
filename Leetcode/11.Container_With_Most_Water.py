class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        ans = (right - left)*min(height[left], height[right])
        while left < right: 
            if height[left] < height[right]: 
                left += 1 
                ans = max(ans, (right-left)*min(height[left], height[right]))
            else:
                right -= 1
                ans = max(ans, (right-left)*min(height[left], height[right]))
        return ans 
            