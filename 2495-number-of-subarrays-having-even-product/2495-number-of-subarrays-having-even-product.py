class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n*(n+1)//2
        tally = 0
        for num in nums:
            if num%2:
                tally += 1
                ans -= tally
            else: tally = 0
        return ans