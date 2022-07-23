class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        left, right = 2, num//2
        while left <= right:
            x = left + (right-left)//2
            if x*x == num:return True
            if x*x < num:
                left = x + 1
            else:
                right = x - 1
        return False