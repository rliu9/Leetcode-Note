class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        n, res, last = len(s), 0, d[s[-1]]
        for i in range(n - 1, -1, -1):
            if d[s[i]] < last:
                res -= d[s[i]]
            else:
                res += d[s[i]]
            last = d[s[i]]
        return res