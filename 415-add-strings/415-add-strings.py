class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(n):
            return ord(n) - ord('0')
        def int2str(n):
            if n == 0: return '0'
            ret = ''
            while n != 0:
                ret += chr(n%10 + 48)
                n //= 10
            return ret[::-1]
        sum1 = sum2 = 0
        for i in num1:sum1 = sum1*10 + str2int(i)
        for j in num2:sum2 = sum2*10 + str2int(j)
        return int2str(sum1+sum2)