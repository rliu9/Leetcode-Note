class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def bt(idx, cur, res):
            res.append(cur)
            for i in range(idx, len(nums)):
                if i!=idx and nums[i] == nums[i-1]:continue
                bt(i+1, cur+[nums[i]], res)
        res = []
        bt(0, [], res)
        return res