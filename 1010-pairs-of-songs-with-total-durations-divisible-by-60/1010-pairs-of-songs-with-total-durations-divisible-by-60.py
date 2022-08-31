class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(int)
        res = 0
        for t in time:
            res += d[(60-t)%60]
            d[t % 60] += 1
        return res