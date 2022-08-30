class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n
        maxArea = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    dp[c] += 1
                else:
                    dp[c] = 0
            maxArea = max(maxArea, self.maxRectangleInHistogram(dp))
        return maxArea

    def maxRectangleInHistogram(self, heights):  # O(N)
        n = len(heights)
        st = [-1]
        maxArea = 0
        for i in range(n):
            while st[-1] != -1 and heights[st[-1]] >= heights[i]:
                currentHeight = heights[st.pop()]
                currentWidth = i - st[-1] - 1
                maxArea = max(maxArea, currentWidth * currentHeight)
            st.append(i)
        while st[-1] != -1:
            currentHeight = heights[st.pop()]
            currentWidth = n - st[-1] - 1
            maxArea = max(maxArea, currentWidth * currentHeight)
        return maxArea