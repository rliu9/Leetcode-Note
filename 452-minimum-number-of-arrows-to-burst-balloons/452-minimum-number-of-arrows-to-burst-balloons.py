class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0
        points = sorted(points, key=lambda x: x[0])

        start = points[0][0]
        end = points[0][1]
        res = 0

        for point in points:
            if point[0] <= end:
                start = max(point[0], start)
                end = min(point[1], end)
            else:
                res += 1
                start = point[0]
                end = point[1]
        return res + 1