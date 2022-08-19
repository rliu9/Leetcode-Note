class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        copy = deque()
        for r in range(n):
            for c in range(n):
                copy.append(matrix[r][c])
        
        for c in range(n-1, -1, -1):
            for r in range(n):
                matrix[r][c] = copy.popleft()
        