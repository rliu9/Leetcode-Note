"""
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] <= nums[-1]:
                r = mid-1
            else:
                l = mid+1
        return nums[l]

# time complexity: O(log n) time
# space complexity O(1)

if __name__ == '__main__':
    ex = Solution()
    assert 1 == ex.findMin([3,4,5,1,2])
    """
    left = 0; right = 8; mid = 4; nums[4] = 8
    -> go right side
    left = 5; right = 8; mid = 6; nums[6] = 1
    -> go left side
    left = 5; right = 5; mid = 5; nums[5] = 0
    -> while loop done -> return 0
    """
    assert 0 == ex.findMin([4,5,6,7,8,0,1,2,3])
