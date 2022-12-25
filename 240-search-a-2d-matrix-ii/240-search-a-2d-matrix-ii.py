class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        x, y = row-1, 0
        while x>=0 and y<col:
            if matrix[x][y] > target: x-=1
            elif matrix[x][y] < target: y+=1
            else:return True
        return False
    
    # O(m+n)
    # O(1)