class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        res = []
        for i in intervals:
            if not res or i[0] > res[-1][-1]:
                res.append(i)
            else:
                res[-1][-1] = max(res[-1][-1], i[1])
        return res