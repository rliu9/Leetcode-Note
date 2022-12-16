class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
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