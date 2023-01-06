class Solution:
    def rob(self, nums: List[int]) -> int:
        def getmax(nums):
            if not nums:return 0
            dp = [nums[0], max(nums[0],nums[1])]
            for i in range(2, len(nums)):
                dp += [max(dp[i-1], dp[i-2]+nums[i])]
            return max(dp[-1],dp[-2])
        return max(nums) if len(nums)<=2 else max(getmax(nums[1:]), getmax(nums[:-1]))
    
    # O(n)
    # O(n)
    
if __name__ == '__main__':
    s = Solution()
    assert s.rob([1,2,3,1]) == 4
    assert s.rob([2,3,2]) == 3