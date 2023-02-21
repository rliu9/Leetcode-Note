class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col, res = len(grid), len(grid[0]), 0
        def bfs(q):
            while q:
                r, c = q.popleft()
                for x,y in (1,0),(0,1),(-1,0),(0,-1):
                    rr, cc = x+r, y+c
                    if 0 <= rr < row and 0 <= cc < col and grid[rr][cc] == '1':
                        grid[rr][cc] = '0'
                        q.append((rr,cc))
                        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    bfs(deque([(r,c)]))
                    res += 1
        return res
    
    # O(mn)
    # O(min(m,n))