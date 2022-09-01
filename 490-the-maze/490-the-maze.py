class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = collections.deque([start])
        rows, cols = len(maze), len(maze[0])
        visit = set()
        while q:
            x, y = q.popleft()
            if x == destination[0] and y == destination[1]:return True
            for dx, dy in (0,1), (1,0), (0,-1), (-1,0):
                i, j = x+dx, y+dy
                while 0<=i<rows and 0<=j<cols and not maze[i][j]:
                    i, j = i+dx, j+dy
                i, j = i-dx, j-dy
                if (i,j) not in visit:
                    visit.add((i,j))
                    q.append((i,j))
        return False