class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(idx, cur):
            res.append(cur[:])
            for i in range(idx, len(nums)):
                cur.append(nums[i])
                backtracking(i+1, cur)
                cur.pop()
        backtracking(0, [])
        return res
    
    # O(n 2^n)
    # O(n)