class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 
    
        d = defaultdict(int)
        _sum = 0
        ans = 0
        for i in nums:
            _sum += i
            if _sum == k: ans += 1
            value = _sum - k
            if value in d: ans += d[value]
            d[_sum] += 1
        return ans
   
