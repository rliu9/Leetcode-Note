import collections

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        q = collections.deque()
        seen = set()
        row,col,count = len(mat),len(mat[0]),0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0: q.append((i,j))
        seen.update(q)
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xx,yy = x+dx,y+dy
                    if xx == row or yy == col or xx < 0 or yy < 0:
                        continue
                    if (xx,yy) in seen:
                        continue
                    seen.add((xx,yy))
                    q.append((xx,yy))
                if mat[x][y] != 0:
                    mat[x][y] += count-1
            count += 1
        return mat

if __name__ == '__main__':
    solution = Solution()
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    assert [[0,0,0],[0,1,0],[0,0,0]] == solution.updateMatrix(mat)
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    assert [[0,0,0],[0,1,0],[1,2,1]] == solution.updateMatrix(mat)
