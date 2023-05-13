class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """n = len(nums)
        prefix, postfix = [1]*n, [1]*n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):
            postfix[j] = postfix[j+1] * nums[j+1]
        return [prefix[i] * postfix[i] for i in range(n)]"""
        n = len(nums)
        prefix = postfix = 1
        res = [1] * n
        for i in range(1, n):
            prefix *= nums[i-1]
            res[i] = prefix
        for i in range(n-2, -1, -1):
            postfix *= nums[i+1]
            res[i] *= postfix
        return res