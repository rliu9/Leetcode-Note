class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        counter = collections.Counter(s)
        for c in counter:
            if counter[c] % 2 == 0:
                res += counter[c]
            else:
                if counter[c] > 2:
                    res += counter[c]-1
        return res if res == len(s) else res + 1