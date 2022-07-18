class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = collections.defaultdict(int)
        for n in nums:d[n] += 1
        pair,remain = 0,0
        for n in d:
            if d[n] % 2 == 0: pair += d[n]//2
            else:
                pair += d[n]//2
                remain += 1
        return [pair,remain]