class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(x)[::-1]) if x >= 0 else int(str(x)[1:][::-1])*-1
        return 0 if res < -2**31 or res > 2**31 else res