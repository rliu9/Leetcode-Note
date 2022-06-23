class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            j = i-1
            while j>=0:   
                if nums[j]<nums[i]:
                    dp[i] = max(dp[j]+1,dp[i])
                j -= 1 
        return max(dp)
    
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    
if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert s.lengthOfLIS([0,1,0,3,2,3]) == 4
    assert s.lengthOfLIS([7,7,7,7,7,7,7]) == 1