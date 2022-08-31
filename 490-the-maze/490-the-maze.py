class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = collections.deque([start])
        visited = set()
        while q:
            i,j = q.popleft()
            if i == destination[0] and j == destination[1]:
                return True
            for di,dj in [[-1,0],[0,-1],[1,0],[0,1]]:
                ni, nj = i + di  , j + dj
                while 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and not maze[ni][nj] :
                    ni, nj  = ni + di , nj + dj
                ni, nj  = ni - di, nj - dj
                if (ni,nj) not in visited:
                    visited.add((ni,nj))
                    q.append((ni,nj))
        return False