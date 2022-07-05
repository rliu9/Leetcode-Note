class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        if not matrix:return 0
        res = 0
        @lru_cache(None)
        def get_len(i,j):
            if 0<=i<row and 0<=j<col and matrix[i][j] == '1':
                return 1+min(get_len(i+1,j), get_len(i,j+1), get_len(i+1,j+1))
            return 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1':
                    res = max(res, get_len(r,c))
        return res**2