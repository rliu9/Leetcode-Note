class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        prevEnd = -float('inf')
        res = 0
        for start,end in sorted(intervals):
            if prevEnd <= start:
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)
                res += 1
        return res
    
    # O(nlogn)
    # O(1)
    """
        intervals.sort(key=lambda x:x[1])
        res = 0
        prevEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
        return res
            