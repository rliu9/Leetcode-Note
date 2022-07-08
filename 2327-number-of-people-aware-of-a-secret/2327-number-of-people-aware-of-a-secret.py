class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * n
        dp[0] = 1
        for i in range(delay, n):
            if i < forget - 1:
                dp[i] = sum(dp[:i-delay+1])
            else:
                dp[i] = sum(dp[i-forget+1:i-delay+1])
        return sum(dp[n-forget:]) % (10**9 + 7)
        