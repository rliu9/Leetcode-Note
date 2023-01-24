class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i, res = 0, 0
        for j in range(len(s)):
            if s[j] in d:
                i = max(i, d[s[j]])
            res = max(res, j-i+1)
            d[s[j]] = j+1
        return res