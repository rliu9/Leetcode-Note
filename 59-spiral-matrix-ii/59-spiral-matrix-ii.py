class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        r,rr,c,cc = 0,n,0,n
        value = 1
        while value <= n**2:
            for i in range(c, cc):
                matrix[r][i] = value
                value += 1
            r += 1
            for i in range(r, rr):
                matrix[i][cc-1] = value
                value += 1
            cc -= 1
            for i in range(cc-1, c-1, -1):
                matrix[rr-1][i] = value
                value += 1
            rr -= 1
            for i in range(rr-1, r-1, -1):
                matrix[i][c] = value
                value += 1
            c += 1
        return matrix