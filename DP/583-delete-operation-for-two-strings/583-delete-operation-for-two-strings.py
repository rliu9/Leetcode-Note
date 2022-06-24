class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # LCS - longest common subsequence
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for j in range(len(word2)-1, -1, -1):
            for i in range(len(word1)-1, -1, -1):
                if word2[j] == word1[i]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        longest_len = dp[0][0]
        return len(word1) - longest_len + len(word2) - longest_len
    
    # Time complexity: O(M*N)
    # Space complexity: O(M*N)