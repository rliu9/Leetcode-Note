"""
You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col,seen,count = len(grid),len(grid[0]),set(),0
        q,fresh = deque(),0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        seen.update(q)
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xx,yy = x+dx,y+dy
                    if xx < 0 or yy < 0 or xx == row or yy == col:
                        continue
                    if (xx,yy) in seen or grid[xx][yy]==0:
                        continue
                    grid[xx][yy] = 2
                    fresh -= 1
                    seen.add((xx,yy))
                    q.append((xx,yy))
            count += 1
        if count > 0: count -= 1
        return count if fresh == 0 else -1

if __name__ == '__main__':
    solution = Solution()
    assert 4 == solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    assert -1 == solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
