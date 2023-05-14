class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = 0
        i = 0
        for j,n in enumerate(s):
            if n in d:
                i = max(d[n], i)
            res = max(j-i+1, res)
            d[n] = j+1
        return res