class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col, q, fresh, seen = len(grid), len(grid[0]), deque([]), 0, set();
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        seen.update(q)
        res = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for i, j in (x+1,y), (x-1,y), (x,y+1), (x,y-1) :
                    if 0 <= i < row and 0 <= j < col and (i,j) not in seen and grid[i][j] != 0:
                        grid[i][j] = 1
                        fresh -= 1
                        seen.add((i,j))
                        q.append((i,j))
            res += 1
        if res > 0:res-=1
        return res if fresh == 0 else -1
    
if __name__ == '__main__':
    solution = Solution()
    assert 4 == solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    assert -1 == solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])