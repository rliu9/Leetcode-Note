class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def bfs(q):
            while q:
                i, j = q.popleft()
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ix, jy = x+i, y+j
                    if not (0<=ix<rows) or not (0<=jy<cols) or grid[ix][jy] == "0":continue
                    q.append((ix, jy))
                    grid[ix][jy] = "0"
                
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(deque([(r,c)]))
                    res += 1
        return res
    
    # O (M*N)
    # O (min(M,N))