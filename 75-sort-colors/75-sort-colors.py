class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = collections.Counter(nums)
        red, white, blue = c[0], c[1], c[2]
        
        nums[:red] = [0] * red
        nums[red:red+white] = [1] * white
        nums[red+white:] = [2] * blue
        
        # O(n)
        # O(n)
        