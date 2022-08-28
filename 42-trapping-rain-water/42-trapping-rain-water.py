class Solution:
    def trap(self, height: List[int]) -> int:
        n, m = len(height), 0
        max_left, max_right, res = [], 0, 0
        for i in range(n):m = max(m, height[i]); max_left.append(m)
        for r in range(n-1, -1, -1):
            max_right = max(max_right, height[r])
            res += min(max_right, max_left[r]) - height[r]
        return res