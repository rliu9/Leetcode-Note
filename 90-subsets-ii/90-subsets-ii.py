class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(idx,cur):
            res.append(cur[:])
            for i in range(idx, len(nums)):
                if i!=idx and nums[i] == nums[i-1]:continue
                cur.append(nums[i])
                backtracking(i+1,cur)
                cur.pop()
        backtracking(0,[])
        return res