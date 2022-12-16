class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        prevEnd = -1
        for start, end in intervals:
            if prevEnd > start:return False
            prevEnd = end
        return True
    
    # O(nlogn)
    # O(1)