class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """cur = res = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], nums[i]+cur)
            res = max(res, cur)
        return res
    
    # O(n)
    # O(1)"""
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)