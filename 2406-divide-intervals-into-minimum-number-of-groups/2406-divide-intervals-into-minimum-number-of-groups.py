class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        end_group = [intervals[0][1]]
        for k in range(1, len(intervals)):
            start, end = intervals[k]
            if end_group and start > end_group[0]:
                heapq.heappop(end_group)
            heapq.heappush(end_group, end)
        return len(end_group)