class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def bfs(i, j):
            grid[i][j] = "0"
            for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
                ix, jy = x+i, y+j
                if not (0 <= ix < rows) or not (0 <= jy < cols) or grid[ix][jy] != "1":continue
                bfs(ix, jy)
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        return res