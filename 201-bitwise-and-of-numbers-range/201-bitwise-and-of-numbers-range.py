class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # find the common 1-bits
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift
    
    """
    The operator & is keeping those bits which is set in both number.
    For several numbers, the operator & is keeping those bits which is 1 in every number.
    In other word, a bit is 0 in any number will result in 0 in the answer's corresponding bit.
    """
    
    # O(1)
    # O(1)