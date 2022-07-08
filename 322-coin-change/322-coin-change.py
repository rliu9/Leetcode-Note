class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = math.inf
        @lru_cache(None)
        def dp(n):
            if n < 0:
                return -1
            if n == 0:
                return 0
            ans = INF
            for m in coins:
                if dp(n-m) >= 0:
                    ans = min(ans, 1 + dp(n-m))
            return ans
        return dp(amount) if dp(amount) < INF else -1
        
        
        """
        #bottom up
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        return -1 if dp[-1] == float('inf') else dp[-1]
    
    # Time complexity: O(n*amount)
    # Space complexity: O(amount)
        """
        