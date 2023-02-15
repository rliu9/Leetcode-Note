class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        q, row, col = deque([]), len(grid), len(grid[0])
        fresh = 0
        res = 0
        visit = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:fresh += 1
                    
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                grid[x][y] = 2
                for r,c in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == 1 and (r,c) not in visit:
                        q.append((r,c))
                        fresh -= 1
                        visit.add((r,c))
            res += 1
        if res == 0:return res if fresh == 0 else -1
        return res-1 if fresh == 0 else -1
        
        
        
        