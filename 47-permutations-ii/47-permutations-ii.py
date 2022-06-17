class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def traverse(path, nums):
            if not nums and path not in res:
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                traverse(path + [nums[i]], nums[:i] + nums[i + 1:])
        traverse([], nums)
        return res