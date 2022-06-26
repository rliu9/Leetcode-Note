class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        # 8=2+6=2+(3+3) dp[8]=max(2,dp[2])*max(6,dp[6])
        for i in range(2,n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j,dp[j])*max(i-j,dp[i-j]))
        return dp[-1]