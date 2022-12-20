class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        def bfs(q):
            while q:
                r, c = q.popleft()
                if 0 <= r < row and 0 <= c < col and grid[r][c] == '1':
                    grid[r][c] = '0'
                    q.append((r+1,c))
                    q.append((r-1,c))
                    q.append((r,c+1))
                    q.append((r,c-1))
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    bfs(deque([(r,c)]))
                    res += 1
        return res