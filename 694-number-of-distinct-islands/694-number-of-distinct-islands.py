class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols, islands = len(grid), len(grid[0]), set()
        def bfs(q, path, start):
            while q:
                x, y = q.popleft()
                ii, jj = start
                for dx, dy in (0,1), (0,-1), (1,0), (-1,0):
                    i, j = dx+x, dy+y
                    if not (0<=i<rows) or not (0<=j<cols) or grid[i][j] != 1:continue
                    q.append((i,j))
                    grid[i][j] = 0
                    path.append((i-ii, j-jj))
    
        for r in range(rows):
            for c in range(cols):
                path = []
                if grid[r][c] == 1:
                    bfs(deque([(r,c)]), path, (r,c))
                    islands.add(tuple(path))
        return len(islands)