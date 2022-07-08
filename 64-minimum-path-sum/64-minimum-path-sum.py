class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[float('inf')] * (col) for _ in range(row)]
        dp[0][0] = grid[0][0]
        
        for r in range(row):
            for c in range(col):
                if r == 0 and c > 0:
                    dp[r][c] = min(dp[r][c], grid[r][c] + dp[r][c-1])
                elif c == 0 and r > 0:
                    dp[r][c] = min(dp[r][c], grid[r][c] + dp[r-1][c])
                else:
                    dp[r][c] = min(dp[r][c], grid[r][c] + min(dp[r-1][c],dp[r][c-1]))
        return dp[-1][-1]
    
    # Time complexity: O(m*n)
    # Space complexity: O(m*n)