class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        square = {}
        nums.sort(reverse = True)
        res = -1
        for num in nums:
            if num * num in square:
                square[num] = square[num * num] + 1
                res = max(res, square[num])
            else:
                square[num] = 1
        return res