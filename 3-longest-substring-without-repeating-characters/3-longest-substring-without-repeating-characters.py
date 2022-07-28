class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, i = 0, 0
        d = {}
        for j in range(len(s)):
            if s[j] in d:
                i = max(i, d[s[j]]+1)
            max_len = max(max_len, j-i+1)
            d[s[j]] = j
        return max_len
            