class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:return m*n
        min_m,min_n = m,n
        for i, j in ops:
            min_m, min_n = min(min_m, i),min(min_n, j)
        return min_m*min_n