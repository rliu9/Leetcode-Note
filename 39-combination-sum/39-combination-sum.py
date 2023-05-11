class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(idx, target, cur, res):
            if target == 0:
                res.append(cur[:])
                return
            if target < 0:return
            for i in range(idx, len(candidates)):
                cur.append(candidates[i])
                bt(i, target-candidates[i], cur, res)
                cur.pop()
        res = []
        bt(0, target, [], res)
        return res
            
    
    # O(2^target)
    # O(max_len_of_combination)