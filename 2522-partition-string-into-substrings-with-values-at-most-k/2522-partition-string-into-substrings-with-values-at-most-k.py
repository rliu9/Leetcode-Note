class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        i, n = 0, len(str(k))
        res = 0
        while i < len(s):
            if int(s[i]) > k:return -1
            else:
                if int(s[i:i+n]) < k:
                    i += n
                else:
                    i += max(n-1, 1)
                res += 1
        return res