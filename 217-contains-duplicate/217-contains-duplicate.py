class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:return True
        return False
    
    # Time Complexity: O(n logn)
    # Space Complexity: O(1)
    
if __name__ == '__main__':
    assert True == Solution().containsDuplicate([1,2,3,1])
    assert True == Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])