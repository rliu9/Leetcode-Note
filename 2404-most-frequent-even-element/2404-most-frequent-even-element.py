class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        for n in nums:
            if n % 2 == 0:d[n] += 1
        d = dict(sorted(d.items(), key=lambda x:-x[1]))
        res, highest = float('inf'), -1
        for i,j in d.items():
            if highest < 0: highest = d[i]
            if d[i] == highest:res = min(res, i)
        return res if res != float('inf') else -1