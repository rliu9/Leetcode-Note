class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:return s
        d = collections.defaultdict(list)
        r, i = 0, 0
        while i < len(s):
            while r < numRows-1 and i < len(s):
                d[r].append(s[i])
                i += 1
                r += 1
            while r > 0 and i < len(s):
                d[r].append(s[i])
                r -= 1
                i += 1
        return ''.join([item for sublist in d.values() for item in sublist])