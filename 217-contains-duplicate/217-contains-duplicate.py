class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
if __name__ == '__main__':
    assert True == Solution().containsDuplicate([1,2,3,1])
    assert True == Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])