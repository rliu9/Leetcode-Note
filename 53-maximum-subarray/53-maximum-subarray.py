class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        # dp
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)
        """
        
        # greedy
        total = 0
        res = nums[0]
        for i in nums:
            total += i
            res = max(res, total)
            if total < 0: total = 0
        return res