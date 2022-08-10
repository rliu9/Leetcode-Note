class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        d = deque()
        res = []
        for i,n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i)
            if d[0] == i-k:
                d.popleft()
            if i >= k-1:
                res.append(nums[d[0]])
        return res