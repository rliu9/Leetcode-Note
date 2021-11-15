class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        points.sort(key=lambda x:x[0]**2+x[1]**2)
        for i in range(k):
            result.append(points[i])
        return result
