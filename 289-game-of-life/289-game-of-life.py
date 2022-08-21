class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l1, l2 = [], []
        row, col = len(board), len(board[0])
        neighbors = [(0,-1),(0,1),(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1)]
        for r in range(row):
            for c in range(col):
                live = 0
                for x, y in neighbors:
                    rr, cc = r+x, c+y
                    if rr<row and rr>=0 and cc<col and cc>=0 and board[rr][cc] == 1:
                        live += 1
                if board[r][c] == 1 and (live < 2 or live > 3):l1.append((r,c))
                if board[r][c] == 0 and live == 3:l2.append((r,c))
        
        for r,c in l1:board[r][c] = 0
        for r,c in l2:board[r][c] = 1
        
                        
                        
                            
                    