class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(idx, cur, res):
            res.append(cur)
            for i in range(idx, len(nums)):
                backtracking(i+1, cur+[nums[i]], res)
        res = []
        backtracking(0, [], res)
        return res