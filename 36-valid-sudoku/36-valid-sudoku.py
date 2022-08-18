class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':continue
                if val in rows[r]:return False
                rows[r].add(val)
                if val in cols[c]:return False
                cols[c].add(val)
                idx = (r//3)*3 + c//3
                if val in boxes[idx]:return False
                boxes[idx].add(val)
        return True
    
    # Time Complexity: O(N^2)
    # Space Complexity: O(N^2)