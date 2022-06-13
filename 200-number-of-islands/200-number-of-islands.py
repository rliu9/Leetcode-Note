class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col,res = len(grid),len(grid[0]),0
        def dfs(i,j):
            if i >= row or j >= col or i < 0 or j < 0 or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x,y = dx+i, dy+j
                dfs(x,y)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i,j)
                    res += 1
        return res
    
    # time complexity: O(M*N)
    # space complexity: O(M*N)