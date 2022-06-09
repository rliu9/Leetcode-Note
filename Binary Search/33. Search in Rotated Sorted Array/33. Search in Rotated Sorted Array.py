class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[-1]:# left is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:# right is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    
    # time complexity: O(log n)
    # space complexity: O(1)
    
if __name__ == '__main__':
    assert 4 == Solution().search([4,5,6,7,0,1,2], 0)
    assert -1 == Solution().search([4,5,6,7,0,1,2], 3)
