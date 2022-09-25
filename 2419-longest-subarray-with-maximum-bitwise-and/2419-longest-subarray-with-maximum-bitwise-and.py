class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, m, count = 0, max(nums), 0
        for n in nums:
            if n == m:
                count+=1
            else:
                count = 0
            res = max(res, count)
        return res