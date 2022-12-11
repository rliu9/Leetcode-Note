class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        for l in grid:
            l.sort()
        while grid[0]:
            temp = 0
            for l in grid:
                temp = max(temp, l.pop())
            res += temp
        return res