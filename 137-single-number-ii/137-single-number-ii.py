class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:d[i] += 1
        return min(d, key=d.get)