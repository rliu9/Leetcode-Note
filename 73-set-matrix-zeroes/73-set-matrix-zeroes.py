class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:zeros.append((i,j))
        for r,c in zeros:
            for i in range(len(matrix)):
                matrix[i][c] = 0
            for j in range(len(matrix[0])):
                matrix[r][j] = 0
        