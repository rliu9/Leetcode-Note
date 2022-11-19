class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        for i in range(2, len(cost)+1):
            x = dp[i-1] + cost[i-1]
            y = dp[i-2] + cost[i-2]
            dp[i] = min(x, y)
        return dp[-1]
        