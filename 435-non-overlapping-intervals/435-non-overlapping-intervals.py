class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prevEnd, res = intervals[0][1], 0
        for interval in intervals[1:]:
            if prevEnd <= interval[0]:
                prevEnd = interval[1]
            else:
                res += 1
                prevEnd = min(prevEnd, interval[1])
        return res
    
    # O(nlogn)
    # O(1)