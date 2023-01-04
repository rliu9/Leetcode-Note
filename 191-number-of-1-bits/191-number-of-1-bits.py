class Solution:
    def hammingWeight(self, n: int) -> int:
        #return("{0:b}".format(n).count('1'))
        
        # n & (n-1) will remove rightmost 1
        # n:1010100    n-1:1010011    n&(n-1):1010000
        res = 0
        while n > 0:
            n = n & (n-1)
            res += 1
        return res
        