class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp,res = 0,0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp += 1
                res += dp
            else:
                dp = 0
        return res
    
    # O(n)
    # O(1)