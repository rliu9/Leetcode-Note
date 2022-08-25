class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total, res, l = 1, [], []
        for i, n in enumerate(nums):
            if n == 0:
                l.append(i)
                continue
            total *= n
        for i, n in enumerate(nums):
            if l and i not in l:res.append(0)
            elif len(l) == 1:
                if i == l[0]:res.append(total)
                else:res.append(0)
            elif len(l) > 1:res.append(0)
            else:res.append(total//n)
        return res