class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp
        """
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp += [max(dp[i-1]+nums[i], nums[i])]
        return max(dp)
        """
    
        # greedy
        cur = 0
        res = nums[0]
        for n in nums:
            cur += n
            res = max(res, cur)
            cur = max(0, cur)
        return res
    
    # O(n)
    # O(1)