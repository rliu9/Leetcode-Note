class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        res,cur = 1,1
        for i,n in enumerate(nums):
            if i >= 1 and n - 1 == nums[i-1]:
                cur += 1
            elif n == nums[i-1]:
                continue
            else:
                cur = 1
            res = max(res, cur)
        return res
        