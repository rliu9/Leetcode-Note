class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(idx,path):
            res.append(path[:])
            for i in range(idx,len(nums)):
                path.append(nums[i])
                backtracking(i+1, path)
                path.pop()
        backtracking(0,[])
        return res
    
    # time complexity: O(N*2^N)
    # space complexity: O(N*2^N)