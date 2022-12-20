class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        def bfs(q):
            ret = 0
            while q:
                r, c = q.popleft()
                if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                    grid[r][c] = 0
                    ret += 1
                    q.append((r+1,c))
                    q.append((r-1,c))
                    q.append((r,c+1))
                    q.append((r,c-1))
            return ret
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    res = max(res, bfs(deque([(r,c)])))
        return res
    
    # O(mn)
    # O(min(m,n))