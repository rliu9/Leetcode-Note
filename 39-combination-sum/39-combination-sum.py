class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(idx, target, cur, res):
            if target == 0:res.append(cur[:]);return
            if target < 0:return
            for i in range(idx, len(candidates)):
                """cur.append(candidates[i])
                backtracking(i, target-candidates[i], cur, res)
                cur.pop()"""
                backtracking(i, target-candidates[i], cur+[candidates[i]], res)
        res = []
        backtracking(0, target, [], res)
        return res
    
    # O(2^target)
    # O(max_len_of_combination)