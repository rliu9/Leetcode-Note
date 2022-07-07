class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = str(math.factorial(n))
        res = 0
        for i in range(len(num)-1, -1,- 1):
            if num[i] != '0':break
            res += 1
        return res