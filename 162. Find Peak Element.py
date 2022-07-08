"""
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, 
or index number 5 where the peak element is 6.
"""

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l,r = 0,len(nums)-1
        while l<r-1:
            mid = (l+r)//2
            # the peak element is strictly greater than its neighbors
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                r = mid-1
        return l if nums[l]>nums[r] else r

# time complexity: O(log n)
# space complexity: O(1)

if __name__ == '__main__':
    solution = Solution()
    assert 2 == solution.findPeakElement([1,2,3,1])
    assert 5 == solution.findPeakElement([1,2,1,3,5,6,4])
