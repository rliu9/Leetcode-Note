class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minCur, maxCur, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            vals = (nums[i], minCur*nums[i], maxCur*nums[i])
            maxCur = max(vals)
            minCur = min(vals)
            res = max(res, maxCur)
        return res