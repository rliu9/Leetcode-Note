class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(start, shape, i, j):
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and grid[i][j] == 1:
                shape.append((i-start[0], j-start[1]))
                grid[i][j] = 0
                dfs(start,shape,i+1,j)
                dfs(start,shape,i-1,j)
                dfs(start,shape,i,j+1)
                dfs(start,shape,i,j-1)
            return shape

        unique_islands = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = tuple(dfs((i,j), [], i, j))
                    unique_islands.add(island)
        return len(unique_islands)