class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if i%3 == 0 and i%2 == 0:res.append(i)
        if not res:return 0
        return sum(res)//len(res)