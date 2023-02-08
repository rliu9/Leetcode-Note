class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols,boxes = [set() for _ in range(9)],[set() for _ in range(9)],[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':continue
                if board[r][c] in rows[r]:return False
                rows[r].add(board[r][c])
                if board[r][c] in cols[c]:return False
                cols[c].add(board[r][c])
                i = (r//3)*3 + c//3
                if board[r][c] in boxes[i]:return False
                boxes[i].add(board[r][c])
        return True
        
    # Time Complexity: O(9^2) = O(1)
    # Space Complexity: O(9^2) = O(1)