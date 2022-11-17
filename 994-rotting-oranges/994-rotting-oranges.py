class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col, seen, q, fresh, count = len(grid), len(grid[0]), set(), deque([]), 0, 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                    seen.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                grid[x][y] = 2
                for r, c in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if 0 <= r < row and 0 <= c < col and (r,c) not in seen and grid[r][c] == 1:
                        q.append((r,c))
                        seen.add((r,c))
                        fresh -= 1
            count += 1
        if count > 0: count -= 1
        return count if fresh == 0 else -1
    
if __name__ == '__main__':
    solution = Solution()
    assert 4 == solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    assert -1 == solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])