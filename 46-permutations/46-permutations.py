class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(cur,counter):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for num in counter:
                if counter[num] > 0:
                    cur.append(num)
                    counter[num] -= 1
                    backtracking(cur, counter)
                    counter[num] += 1
                    cur.pop()
        backtracking([],Counter(nums))
        return res