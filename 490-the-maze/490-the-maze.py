class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = collections.deque([start])
        rows, cols = len(maze), len(maze[0])
        visit = set()
        while q:
            x, y = q.popleft()
            if [x,y] == destination:return True
            for dx, dy in (0,1), (1,0), (0,-1), (-1,0):
                i, j = x+dx, y+dy
                while 0<=i<rows and 0<=j<cols and maze[i][j] != 1:
                    i, j = i+dx, j+dy
                i, j = i-dx, j-dy
                if (i,j) not in visit:
                    visit.add((i,j))
                    q.append((i,j))
        return False