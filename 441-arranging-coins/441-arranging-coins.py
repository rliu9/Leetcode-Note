class Solution:
    def arrangeCoins(self, n: int) -> int:
        # binary search
        left, right = 0, n
        while left <= right:
            mid = (left+right) // 2
            cur = mid*(mid+1) // 2
            if cur < n:
                left = mid + 1
            elif cur > n:
                right = mid - 1
            else:
                return mid
        return right