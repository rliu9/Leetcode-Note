class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)-1
        max_area = 0
        left,right = 0, n
        while (left < right):
            area = (right-left) * min(height[left],height[right])
            max_area = max(max_area, area)
            if height[left] < height[right]: left+=1
            else: right-=1
        return max_area
    
    # time complexity: O(n)
    # space complexity: O(1)
