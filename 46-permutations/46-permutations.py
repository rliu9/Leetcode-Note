class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(cur, counter):
            if len(cur) == len(nums):
                res.append(cur[:])
            for c in counter:
                if counter[c] > 0:
                    cur.append(c)
                    counter[c] -= 1
                    backtracking(cur, counter)
                    counter[c] += 1
                    cur.pop()
        backtracking([], collections.Counter(nums))
        return res