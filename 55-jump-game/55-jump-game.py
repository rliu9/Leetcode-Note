class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n,idx = len(nums)-1,len(nums)-1
        for i in range(n,-1,-1):
            if nums[i]+i >= idx:
                idx = i
        return idx==0
        
    # O(n)
    # O(1)