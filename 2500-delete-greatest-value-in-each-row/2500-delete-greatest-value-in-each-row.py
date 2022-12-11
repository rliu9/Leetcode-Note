class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for l in grid:l.sort()
        return sum(max(i) for i in zip(*grid))