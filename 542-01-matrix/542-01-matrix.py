class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # bfs
        q, visited = deque([]), set()
        row, col, count = len(mat), len(mat[0]), 0
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xx,yy = x+dx,y+dy
                    if xx >= row or yy >= col or xx < 0 or yy < 0 or (xx,yy) in visited:
                        continue
                    visited.add((xx,yy))
                    q.append((xx,yy))
                if mat[x][y] != 0:
                    mat[x][y] = count
            count += 1
        return mat
                            
                        