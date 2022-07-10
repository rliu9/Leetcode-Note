class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[-1] = True
        for i in range(n-2,-1,-1):
            dp[i] = any(dp[i:i+nums[i]+1])
        return dp[0]
    # O(n)
    # O(n)