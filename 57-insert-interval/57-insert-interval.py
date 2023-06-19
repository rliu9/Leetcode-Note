class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.append(newInterval)
        intervals.sort()
        for interval in intervals:
            if not res or interval[0] > res[-1][-1]:
                res.append(interval)
            else:
                res[-1][-1] = max(res[-1][-1], interval[-1])
        return res
        
        
    # O(nlogn)
    # O(n)
if __name__ == '__main__':
    s = Solution()
    assert s.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]