class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)-1
        max_right = heights[n]
        ans = []
        ans.append(n)
        for i in range(n-1, -1, -1):
            if heights[i] > max_right: ans.append(i)
            max_right = max(max_right, heights[i])
        return sorted(ans)
