class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        self.i = 1
        def dfs(r, c, going_up):
            if 0 <= r < n and 0 <= c < n and res[r][c] == 0:
                res[r][c] = self.i
                self.i += 1
                if going_up:
                    dfs(r-1, c, True)
                dfs(r, c+1, False)
                dfs(r+1, c, False)
                dfs(r, c-1, False)
                dfs(r-1, c, True)
        dfs(0, 0, False)
        return res