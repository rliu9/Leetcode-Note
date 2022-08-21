class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        neighbors = [(0,-1),(0,1),(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1)]
        for r in range(row):
            for c in range(col):
                live = 0
                for x, y in neighbors:
                    rr, cc = r+x, c+y
                    if rr<row and rr>=0 and cc<col and cc>=0 and abs(board[rr][cc]) == 1:
                        live += 1
                if board[r][c] == 1:
                    if live < 2 or live > 3:board[r][c] = -1
                else:
                    if live == 3:board[r][c] = 2
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 2:board[r][c] = 1
                elif board[r][c] == -1:board[r][c] = 0
        
        # O(M*N)
        # O(1)
                        
                            
                    