class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(idx, target, cur, res):
            if target == 0:
                res.append(cur)
            if target < 0:return
            for i in range(idx, len(candidates)):
                bt(i, target-candidates[i], cur+[candidates[i]], res)
        res = []
        bt(0, target, [], res)
        return res
    
    # O(2^target)
    # O(max_len_of_combination)