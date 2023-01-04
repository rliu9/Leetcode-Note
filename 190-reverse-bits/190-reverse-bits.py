class Solution:
    def reverseBits(self, n: int) -> int:        
        # return int('{0:032b}'.format(n)[::-1], 2)
        res = 0
        for i in range(32):
            if n & 1:
                res += 1 << (31-i)
            n >>= 1
        return res
    
    # O(1)
    # O(1)