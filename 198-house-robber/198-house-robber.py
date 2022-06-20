class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return max(dp[-1],dp[-2])
    
    # time complexity: O(n)
    # space complexity: O(n)
    
if __name__ == '__main__':
    s = Solution()
    nums1,answer1 = [1,2,3,1],4
    nums2,answer2 = [2,7,9,3,1],12
    assert answer1 == s.rob(nums1)
    assert answer2 == s.rob(nums2)