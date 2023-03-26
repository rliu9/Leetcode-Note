class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # LCS - longest common subsequence
        # dp
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for j in range(n2-1, -1, -1):
            for i in range(n1-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        lcs = dp[0][0]
        return n1+n2-2*lcs
    
    # Time complexity: O(M*N)
    # Space complexity: O(M*N)