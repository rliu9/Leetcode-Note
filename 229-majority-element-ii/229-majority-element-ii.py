class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        time = len(nums)/3
        res = set()
        count,start = 0,nums[0]
        for i in range(len(nums)):
            if start == nums[i]:
                count += 1
            else:
                start = nums[i]
                count = 1
            if count > time:
                res.add(nums[i])
        return list(res)