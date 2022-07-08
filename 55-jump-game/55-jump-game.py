class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i,j = len(nums)-1,len(nums)-1
        while i>=0:
            if i + nums[i] >= j:
                j = i
            i -= 1
        return j==0
    
    # O(n)
    # O(1)