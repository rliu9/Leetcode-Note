class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(index, cur):
            if sum(cur) == target:
                res.append(cur[:])
                return
            if sum(cur) > target:
                return
            for i in range(index, len(candidates)):
                #if candidates.count(candidates[i]) < 2:
                cur.append(candidates[i])
                backtracking(i, cur)
                cur.pop()
        backtracking(0, [])
        return res