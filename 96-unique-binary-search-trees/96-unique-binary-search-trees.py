class Solution:
    def numTrees(self, n: int) -> int:
        """numTrees[4] =
                numTrees[0]*numTrees[3] + 
                numTrees[1]*numTrees[2] +
                numTrees[2]*numTrees[1] +
                numTrees[3]*numTrees[0]"""
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[-1]
    
    # O(n^2)
    # O(n)