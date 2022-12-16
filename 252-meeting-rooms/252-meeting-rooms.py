class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        prevEnd = -1
        for interval in sorted(intervals):
            if prevEnd > interval[0]:return False
            prevEnd = interval[1]
        return True
    
    # O(logn)
    # O(1)