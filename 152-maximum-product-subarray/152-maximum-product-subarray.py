class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_sofar, max_sofar, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            vals = (nums[i], nums[i]*min_sofar, nums[i]*max_sofar)
            min_sofar, max_sofar = min(vals), max(vals)
            res = max(res, max_sofar)    
        return res