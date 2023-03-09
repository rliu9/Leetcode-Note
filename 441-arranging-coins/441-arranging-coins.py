class Solution:
    def arrangeCoins(self, n: int) -> int:
        cur = 1
        while n > cur:
            n -= cur
            cur += 1
        return cur-1 if cur != n else cur