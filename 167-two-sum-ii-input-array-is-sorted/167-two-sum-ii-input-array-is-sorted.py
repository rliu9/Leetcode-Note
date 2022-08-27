class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:return[l+1,r+1]
            if s < target:l += 1
            else:r -= 1
        return -1
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    
if __name__ == '__main__':
    assert Solution().twoSum([2,7,11,15], 9) == [1,2]
    assert Solution().twoSum([2,3,4], 6) == [1,3]
    assert Solution().twoSum([-1,0], -1) == [1,2]
                