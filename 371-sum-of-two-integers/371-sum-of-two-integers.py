class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        # works both as while loop and single value check 
        while (b & mask) > 0:
            carry = ( a & b ) << 1
            a ^= b
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a