class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        rr = [i for i in range(r) for j in range(c) if grid[i][j] == 1]
        cc = [j for j in range(c) for i in range(r) if grid[i][j] == 1]
        
        median_pos = len(rr) // 2
        mi, mj = rr[median_pos], cc[median_pos]
        
        return sum(abs(x-mi) for x in rr) + sum(abs(x-mj) for x in cc)