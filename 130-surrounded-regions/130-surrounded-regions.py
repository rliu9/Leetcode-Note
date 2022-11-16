class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        def dfs(r,c):
            board[r][c] = '.'
            for ri, rj in (0,1),(1,0),(-1,0),(0,-1):
                i, j = r+ri, c+rj
                if 0 <= i < row and 0 <= j < col and board[i][j] == 'O':
                    dfs(i,j)
        
        for r in [0, row-1]:
            for c in range(col):
                if board[r][c] == 'O':dfs(r,c)
        
        for r in range(row):
            for c in [0, col-1]:
                if board[r][c] == 'O':dfs(r,c)
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == '.':board[r][c] = 'O'
                elif board[r][c] == 'O':board[r][c] = 'X'
        