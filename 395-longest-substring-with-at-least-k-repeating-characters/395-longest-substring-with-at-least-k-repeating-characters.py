class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        c = collections.Counter(s)
        for i, n in enumerate(s):
            if c[n] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)
        return len(s)
    
    # O(n^2)
    # O(n)