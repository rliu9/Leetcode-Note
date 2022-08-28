class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, res = 0, len(height)-1, 0
        while l < r:
            res = max(res, min(height[l],height[r])*(r-l))
            if height[l] < height[r]:l += 1
            else:r -= 1
        return res
    
    # O(n)
    # O(1)