class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        def dfs(r, c, going_up, res):
            if 0 <= r < row and 0 <= c < col and matrix[r][c] != '.':
                res.append(matrix[r][c])
                matrix[r][c] = '.'
                if going_up:
                    dfs(r-1, c, going_up, res)
                dfs(r, c+1, False, res)
                dfs(r+1, c, False, res)
                dfs(r, c-1, False, res)
                dfs(r-1, c, True, res)
        res = []
        dfs(0, 0, True, res)
        return res
    