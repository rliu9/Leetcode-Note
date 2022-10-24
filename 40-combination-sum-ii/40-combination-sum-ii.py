class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def bt(idx, cur, res, target):
            if target == 0:
                res.append(cur)
            if target < 0:return
            for i in range(idx, len(candidates)):
                if i!=idx and candidates[i] == candidates[i-1]:continue
                bt(i+1, cur+[candidates[i]], res, target-candidates[i])
        res = []
        bt(0, [], res, target)
        return res