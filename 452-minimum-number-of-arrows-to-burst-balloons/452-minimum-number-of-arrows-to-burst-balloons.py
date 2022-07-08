class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:return 0
        points = sorted(points, key=lambda x:x[0])
        start,end,res = points[0][0],points[0][1],0
        for s,e in points:
            if s <= end:
                start = max(start, s)
                end = min(end, e)
            else:
                res += 1
                start = s
                end = e
        return res+1
    
    # Time complexity: O(n logn)
    # Space complexity: O(n)
    
if __name__ == '__main__':
    s = Solution()
    assert s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
    assert s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4
    assert s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2