class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxwater = 0

        while l < r:

            if height[l] <= height[r]:
                length = r - l 
                width = min(height[l], height[r])
                maxwater = max(maxwater, length * width)
                l += 1
            else: 
                length = r - l 
                width = min(height[l], height[r])
                maxwater = max(maxwater, length * width)
                r -= 1
        return maxwater
