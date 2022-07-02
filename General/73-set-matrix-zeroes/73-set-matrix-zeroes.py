class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros_row, zeros_col = set(), set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeros_row.add(row)
                    zeros_col.add(col)
                    
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in zeros_row or c in zeros_col:
                    matrix[r][c] = 0
                    
        # Time Complexity: O(M*N)
        # Space Complexity: O(M+N)