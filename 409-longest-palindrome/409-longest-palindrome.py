class Solution:
    def longestPalindrome(self, s: str) -> int:
        char = {}
        for i in s:
            if i not in char:
                char[i] = 1
            else:
                char[i] += 1
        res = 0
        for c in char:
            if char[c] % 2 == 0:
                res += char[c]
            else:
                if char[c] > 2:
                    res += char[c]-1
        return res + 1 if len(s) > res else res
                    