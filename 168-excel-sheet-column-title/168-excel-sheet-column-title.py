class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n > 0:
            n -= 1
            n, i = divmod(n, 26)
            res += chr(65+i)
        return res[::-1]
            