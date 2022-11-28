class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        def dfs(res, r, c, going_up):
            if 0 <= r < row and 0 <= c < col and matrix[r][c] != '.':
                res.append(matrix[r][c])
                matrix[r][c] = '.'
                if going_up:
                    dfs(res, r-1, c, True)
                dfs(res, r, c+1, False)
                dfs(res, r+1, c, False)
                dfs(res, r, c-1, False)
                dfs(res, r-1, c, True)
        res = []
        dfs(res, 0, 0, False)
        return res