class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a xor 0 = a
        # a xor a = 0
        a = 0
        for n in nums:
            a ^= n
        return a
    
    # O(n)
    # O(1)