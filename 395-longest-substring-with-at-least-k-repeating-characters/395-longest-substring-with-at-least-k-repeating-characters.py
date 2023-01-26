class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        c = collections.Counter(s)
        for i, n in enumerate(s):
            if c[n] < k:
                return max(self.longestSubstring(s[:i], k), self.longestSubstring(s[i+1:], k))
        return len(s)