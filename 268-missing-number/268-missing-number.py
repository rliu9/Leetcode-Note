class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, n in enumerate(nums):
            res ^= i ^ n
        return res
        """
        n = len(nums)
        return ((n * (n+1)) // 2) - sum(nums)
        # O(n)
        # O(1)
        """