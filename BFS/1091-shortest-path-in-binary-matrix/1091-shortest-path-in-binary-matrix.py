class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid)-1, len(grid[0])-1
        if grid[0][0] != 0 or grid[row_len][col_len] != 0:
            return -1
        directions = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        q = deque([(0,0)])
        grid[0][0] = 1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                distance = grid[r][c]
                if r == row_len and c == col_len:return distance
                for dr,dc in directions:
                    rr,cc = r+dr, c+dc
                    if rr < 0 or cc < 0 or rr > row_len or cc > col_len:
                        continue
                    if grid[rr][cc] != 0:
                        continue
                    grid[rr][cc] = distance + 1
                    q.append((rr,cc))
        return -1
    # time complexity: O(n)
    # space complexity: o(n)
    
    
                
                