class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col, res = len(grid), len(grid[0]), 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    q = deque([(r,c)])
                    res += 1
                    while q:
                        x, y = q.popleft()
                        if 0 <= x < row and 0 <= y < col and grid[x][y] == '1':
                            grid[x][y] = '0'
                            q.append((x+1,y))
                            q.append((x-1,y))
                            q.append((x,y+1))
                            q.append((x,y-1))     
        return res