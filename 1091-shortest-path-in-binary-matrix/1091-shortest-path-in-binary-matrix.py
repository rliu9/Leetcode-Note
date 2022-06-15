class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row,max_col = len(grid)-1,len(grid[0])-1
        directions=[
            (1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)
        ]
        def get_neighbours(row,col):
            for r,c in directions:
                rr,cc = r+row,c+col
                if not (0<=rr<=max_row and 0<=cc<=max_col):
                    continue
                if grid[rr][cc] != 0:
                    continue
                yield (rr,cc)
            
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        q = deque()
        q.append((0,0))
        grid[0][0] = 1
        while q:
            row,col = q.popleft()
            distance = grid[row][col]
            if (row,col) == (max_row,max_col):return distance
            for row_neighbour,col_neighbour in get_neighbours(row,col):
                grid[row_neighbour][col_neighbour] = distance + 1
                q.append((row_neighbour,col_neighbour))
        return -1
    
    # time complexity: O(n)
    # space complexity: o(n)
    
    
                
                