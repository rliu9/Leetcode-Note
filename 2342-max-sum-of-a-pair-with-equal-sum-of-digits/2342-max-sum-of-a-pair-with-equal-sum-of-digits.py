class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_sum(n):
            ret = 0
            for i in str(n):ret+=int(i)
            return ret
        d,res = collections.defaultdict(list),-1
        for i in nums:d[get_sum(i)].append(i)
        for key in d:
            d[key].sort()
            if len(d[key])>=2:
                res = max(res,d[key].pop()+d[key].pop())
        return res
                