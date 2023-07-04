class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        #dfs
        def dfs(r, c):
            if 0 <= r < row and 0 <= c < col and grid[r][c] == '1':
                grid[r][c] = '0'
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        return res
            