class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        hashtb = {}
        for i, n in enumerate(nums):
            if target-n in hashtb:
                return [hashtb[target-n], i]
            hashtb[n] = i
            
    # Time Complexity: O(n)
    # Space Complexity: O(n)