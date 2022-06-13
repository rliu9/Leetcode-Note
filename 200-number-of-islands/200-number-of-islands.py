class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        """
        DFS:
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
        """
    
    # time complexity: O(M*N)
    # space complexity: O(M*N)
    
        #BFS: 
        row,col,count = len(grid),len(grid[0]),0
        def bfs(q):
            while q:
                for _ in range(len(q)):
                    x,y = q.popleft()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        xx,yy = x+dx,y+dy
                        if xx < 0 or yy < 0 or xx == row or yy == col or grid[xx][yy]=='0':
                            continue
                        grid[xx][yy] = '0'
                        q.append((xx,yy))
                        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    bfs(deque([(i,j)]))
                    count += 1    
        return count
    
    # time complexity: O(M*N)
    # Maximum siblings in queue will be min(M, N). So space complexity is min(M,N)