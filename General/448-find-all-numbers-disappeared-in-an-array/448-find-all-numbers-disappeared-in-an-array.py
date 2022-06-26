class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in counter:
                res.append(i)
        return res