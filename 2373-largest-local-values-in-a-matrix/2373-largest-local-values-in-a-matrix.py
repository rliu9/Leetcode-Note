class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
        matrix = [[0]*n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                matrix[r][c] = max(grid[r][c],grid[r+1][c],grid[r+2][c],grid[r][c+1],grid[r][c+2],grid[r+1][c+1],grid[r+1][c],grid[r+1][c+2],grid[r+2][c+1],grid[r+2][c+2])
        return matrix