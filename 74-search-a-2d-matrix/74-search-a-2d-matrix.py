class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        for col in zip(*matrix):
            for item in col:
                if item > target:
                    break
                row += 1
            break
        left, right = 0, len(matrix[0])-1
        if row > 0:
            row -= 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True
        return False
            