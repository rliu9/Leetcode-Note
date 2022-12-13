class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:return True
            hashset.add(n)
        return False
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
if __name__ == '__main__':
    assert True == Solution().containsDuplicate([1,2,3,1])
    assert True == Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])