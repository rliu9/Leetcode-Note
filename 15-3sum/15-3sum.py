class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, s = set(), set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if -(nums[i]+nums[j]) in s:
                    res.add((nums[i], nums[j], -(nums[i]+nums[j])))
            s.add(nums[i])
        return list(res)