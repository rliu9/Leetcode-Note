class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(cur, idx, remain):
            if remain == 0:
                res.append(cur[:])
                return
            if remain < 0:
                return
            for i in range(idx, len(candidates)):
                if i != idx and candidates[i] == candidates[i-1]:continue
                cur.append(candidates[i])
                remain-=candidates[i]
                backtracking(cur, i+1, remain)
                remain+=candidates[i]
                cur.pop()
        backtracking([],0,target)
        return res
    
    # O(2^N)
    # O(N)
    
"""
Notice that every time we enter the loop in combine_sum_2, the first iteration of the loop always     skips over the condition to continue to the loop and goes straight into the recursive function at     the end of the loop. So as we go further into the recursion stack, we always account for               duplicates. then when each layer of recursion finishes, instead of looping through the rest of the     array, we just ignore the duplicates since we've already seen them, and shouldn't repeat work again.
"""