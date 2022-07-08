class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur, counter):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for num in counter:
                if counter[num] > 0:
                    cur.append(num)
                    counter[num] -= 1
                    backtrack(cur, counter)
                    cur.pop()
                    counter[num] += 1
        backtrack([], Counter(nums))
        return res
    
    # O(N!)
    # O(N)